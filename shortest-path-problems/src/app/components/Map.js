// src/app/components/Map.js

import { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { getShortestPath } from '../utils/api';

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

  // Effect to fetch data when the selected algorithm, source, destination, or k changes
  useEffect(() => {
    if (algorithm && source && destination) {
      const fetchData = async () => {
        const data = await getShortestPath(algorithm, source, destination, k);
        
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

  return (
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
              <Marker key={index} position={[point.latitude, point.longitude]} icon={icon} />
            ))}
            {/* Draw a polyline to connect the points in this path */}
            {/* <Polyline
              positions={pathData.path.map(point => [point.latitude, point.longitude])}
              color={pathIndex === 0 ? 'blue' : 'red'} // Alternate colors for different paths
            /> */}
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
        <p>Total Time: {time.toFixed(2)} seconds</p>
      </div>
    </div>
  );
};

export default Map;
