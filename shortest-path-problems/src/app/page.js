"use client"

import { useState } from 'react';
// Dynamically import Map with client-side only rendering
const Map = dynamic(() => import('./components/Map'), { ssr: false });
import dynamic from 'next/dynamic';
import Header from './components/Header';
import Footer from './components/Footer';


export default function HomePage() {
  // States for algorithm selection, source/destination points, and k value
  const [algorithm, setAlgorithm] = useState('');
  const [source, setSource] = useState(106); // Default source point
  const [destination, setDestination] = useState(107); // Default destination point
  const [k, setK] = useState(5); // Default value for k in Yen's Algorithm

  return (
    <div className="container mx-auto p-8">
      <Header/>
      
      <h1 className="text-2xl font-bold mb-4">Shortest Path Visualization</h1>

      {/* Dropdown to select the algorithm */}
      <div className="mb-4">
        <label className="block text-gray-700">Select Algorithm:</label>
        <select
          value={algorithm}
          onChange={(e) => setAlgorithm(e.target.value)}
          className="border rounded p-2 w-full"
        >
          <option value="">-- Select Algorithm --</option>
          <option value="dijkstra">Dijkstra</option>
          <option value="bellmanFord">Bellman-Ford</option>
          <option value="floydWarshall">Floyd-Warshall</option>
          <option value="yen">Yen (Top k shortest paths)</option>
        </select>
      </div>

      {/* Input for source vertex */}
      <div className="mb-4">
        <label className="block text-gray-700">Source Vertex ID:</label>
        <input
          type="number"
          value={source}
          onChange={(e) => setSource(Number(e.target.value))}
          className="border rounded p-2 w-full"
        />
      </div>

      {/* Input for destination vertex */}
      <div className="mb-4">
        <label className="block text-gray-700">Destination Vertex ID:</label>
        <input
          type="number"
          value={destination}
          onChange={(e) => setDestination(Number(e.target.value))}
          className="border rounded p-2 w-full"
        />
      </div>

      {/* Input for k value if Yen's algorithm is selected */}
      {algorithm === 'yen' && (
        <div className="mb-4">
          <label className="block text-gray-700">K (Number of paths for Yen's Algorithm):</label>
          <input
            type="number"
            value={k}
            onChange={(e) => setK(Number(e.target.value))}
            className="border rounded p-2 w-full"
          />
        </div>
      )}

      {/* Render the Map component with selected options */}

      
      <Map algorithm={algorithm} source={source} destination={destination} k={k} />
      <Footer/>
      
    </div>
  );
}
