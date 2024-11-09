// src/app/components/Map.js

import { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Polyline, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { getShortestPath } from '../utils/api';
import { getGraphData } from '../utils/api'; // Import the graph function

// Define a custom icon for markers
const icon = new L.Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/684/684908.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});

const Map = ({ algorithm, source, destination, k }) => {
  // State to store the paths, distances, and time
  const [paths, setPaths] = useState([]);
  const [time, setTime] = useState(0);
  const colors = ['blue', 'red', 'green', 'purple', 'pink'];
  const [nodes, setNodes] = useState([]); // State for nodes
  const [edges, setEdges] = useState([]); // State for edges

  // Effect to fetch data when the selected algorithm, source, destination, or k changes
  useEffect(() => {
    if (algorithm && source && destination) {
      const fetchData = async () => {
        const data = await getShortestPath(algorithm, source, destination, k);
        console.log(data);
        
        if (data) {
          if (algorithm === 'yen') {
            setPaths(data.result); // Set multiple paths for Yen
          } else {
            setPaths([data.result]); // Set a single path for other algorithms
          }
          setTime(data.elapsedTime || 0); // Set time for all algorithms
        } else {
          // Reset values if no data
          setPaths([]);
          setTime(0);
        }
      };
      fetchData();
    }
  }, [algorithm, source, destination, k]);

  useEffect(() => {
    const fetchData = async () => {
      const graphData = await getGraphData();
      if (graphData) {
        setNodes(graphData.vertices); // Set nodes from the vertices array
        setEdges(graphData.edges); // Set edges from the edges array
      }
    };
    fetchData();
  }, []);

  return (
    <>
    <div>
      {/* Map container with Leaflet */}
      <MapContainer center={[10.772055, 106.657826]} zoom={13} style={{ height: '500px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />

        {/* Render markers and paths for each path in Yen's result */}
        {paths.map((pathData, pathIndex) => (
          <div key={pathIndex}>
            {/* Display each point in the path with a marker */}
            {pathData.path.map((point, index) => (
              <Marker key={index} position={[point.latitude, point.longitude]} icon={icon}><Popup>{point.id}</Popup></Marker>
            ))}
            {/* Draw a polyline to connect the points in this path */}
            
            <Polyline
                positions={pathData.path.map(point => [point.latitude, point.longitude])}
                color={colors[pathIndex % colors.length]} // Cycle through colors
                />
          </div>
        ))}
      </MapContainer>
      
      {/* Display distances and time for each path below the map */}
      <div className="mt-4">
        {paths.map((pathData, index) => (
          <p key={index}>Path {index + 1} Distance: {pathData.distance} meters</p>
        ))}
        <p>Total Time: {time.toFixed(6)} seconds</p>
        {paths.map((pathData, index) => (
          <p key={index}> 
            Path {index + 1} IDs: {pathData.path.map(point => point.id).join(', ')}
          </p>
        ))}
      </div>
    </div>
    <div>
    <div className="bg-gray-100 p-4 mt-4 rounded">
    <h2 className="text-xl font-semibold mb-2">Graph Section Overview</h2>
    <p>This section displays all nodes in the graph, with each node's ID shown below:</p>
    <p className="mt-2 font-medium">Node IDs: {nodes.map(node => node.id).join(", ")}</p>
  </div>
      <MapContainer center={[10.772055, 106.657826]} zoom={13} style={{ height: '500px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />

        {/* Display nodes with popups */}
        {nodes.map(node => (
          <Marker key={node.id} position={[node.latitude, node.longitude]} icon={icon}>
            <Popup>ID: {node.id}</Popup>
          </Marker>
        ))}

        {/* Display edges as polylines */}
        {edges.map((edge, index) => (
          <Polyline
            key={index}
            positions={[
              [edge.source.latitude, edge.source.longitude],
              [edge.destination.latitude, edge.destination.longitude]
            ]}
            color="gray"
          />
        ))}
      </MapContainer>
    </div>
    </>
  );
};

export default Map;
