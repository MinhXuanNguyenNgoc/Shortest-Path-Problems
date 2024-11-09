
import axios from 'axios';

// This is the Function to fetch the shortest path data for each algorithm
export const getShortestPath = async (algorithm, source, destination, k = 5) => {
  // We define endpoints based on the algorithm
  const endpoints = {
    dijkstra: `/dijkstra?source_vertex=${source}&destination_vertex=${destination}`,
    bellmanFord: `/bellman-ford?source_vertex=${source}&destination_vertex=${destination}`,
    floydWarshall: `/floyd-warshall?source_vertex=${source}&destination_vertex=${destination}`,
    yen: `/yen?source_vertex=${source}&destination_vertex=${destination}&k=${k}`,
  };

  try {
    // Make a GET request to the appropriate endpoint
    const response = await axios.get(`http://localhost:8000${endpoints[algorithm]}`);
    return response.data; // Return the data from the response
  } catch (error) {
    console.error(`Error fetching data from ${algorithm} endpoint:`, error);
    return null; // Return null if there's an error
  }
};
