# File for managing OpenStreetMaps data

import xml.etree.ElementTree as ET
import csv
import haversine as hs   
from haversine import Unit

def calculate_distance(coordinate1, coordinate2):
    return int(hs.haversine(coordinate1,coordinate2,unit=Unit.METERS))

def extract_nodes_from_osm_file(osm, input_type='file'):
    """
    This method reads the passed osm file (xml) and finds intersections (nodes that are shared by two or more roads) 
    which are the nodes for our adjacency matrix

    :param osm: An osm file or a string from get_osm()

    :return: Array containing coordinates of all intersections found in the passed osm file
    """
    intersection_coordinates = []
    if input_type == 'file':
        tree = ET.parse(osm)
        root = tree.getroot()
        children = list(root)
    elif input_type == 'str':
        tree = ET.fromstring(osm)
        children = tree.getchildren()

    counter = {}
    for child in children:
        if child.tag == 'way':
            # Check if the way represents a "highway (road)"
            # If the way that we are focusing right now is not a road,
            # continue without checking any nodes
            road = False
            road_types = ('primary', 'secondary', 'residential', 'tertiary', 'service') 
            for item in child:
                if item.tag == 'tag' and item.attrib['k'] == 'highway' and item.attrib['v'] in road_types: 
                    road = True

            if not road:
                continue

            for item in child:
                if item.tag == 'nd':
                    nd_ref = item.attrib['ref']
                    if not nd_ref in counter:
                        counter[nd_ref] = 0
                    counter[nd_ref] += 1

    # Find nodes that are shared with more than one way, which
    # might correspond to intersections
    intersections = []
    for x in counter:
        if counter[x] > 1:
            intersections.append(x)

    # Extract intersection coordinates
    for child in children:
        if child.tag == 'node' and child.attrib['id'] in intersections:
            coordinate = (float(child.attrib['lat']), float(child.attrib['lon']))
            intersection_coordinates.append(coordinate)
    return intersection_coordinates

def write_to_csv(result):
    """
    This method writes the resulting intersections to a csv file, so it can be displayed for debugging purposes on https://umap.openstreetmap.fr/de/

    :param result: A list of intersections coordinates represented as a string e.g. ["106.54545,50.645645", "107.86745,50.6457455"]
    """
    with open('intersectionsNew.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["lat", "lon"]

        writer.writerow(field)
        for x in result:
            writer.writerow(x)



def read_from_csv(path):
    """
    This method reads a cvs file with lat,lon coordinates

    :param path: The path where to find the csv file to read from

    :return: A list of coordinates e.g. [(106.5455434,10.4554545),(...)]
    """
    nodes = []
    with open(path, mode ='r') as file:
        csvFile = csv.reader(file)
        skip = True
        for lines in csvFile:
            if skip:
                skip = False
                continue
            nodes.append((float(lines[0]),float(lines[1])))
    
    return nodes