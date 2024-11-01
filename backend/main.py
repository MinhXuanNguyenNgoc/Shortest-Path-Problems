"""API"""

from fastapi import FastAPI, Query
from starlette import status
from typing import List

from models.result import SinglePathResultViewModel, MultiplePathsResultViewModel
from services.utils import adjacency_matrix, nodes, index_hcmut, index_sheraton
from services import bellman_ford as BellmanFordService
from services import dijkstra as DijKStraService
from backend.services import floyd_warshall as FloydWarshallService
from services import yen as YenService

app = FastAPI()

@app.get("/", tags=["Health Check"], status_code=status.HTTP_200_OK, response_model=str)
async def health_check():
    """
    Endpoint for checking the health status of the API service.

    Returns:
        str: A message indicating that the API service is up and running.

    """
    return "API Service is up and running!"

@app.get("/dijkstra", tags=["Dijkstra Algorithm"], status_code=status.HTTP_200_OK, response_model=SinglePathResultViewModel)
async def dijkstra():
    """
    Endpoint for getting the result of the Dijkstra algorithm.

    Returns:
        result (SinglePathResultViewModel): Result containing list of coordinates
        representing the shortest path from HCMUT to Sheraton Hotel.
    """
    return DijKStraService.get_shortest_path(adjacency_matrix, nodes, index_hcmut, index_sheraton)

@app.get("/bellman-ford", tags=["Bellman-Ford Algorithm"], status_code=status.HTTP_200_OK, response_model=SinglePathResultViewModel)
async def bellman_ford():
    """
    Endpoint for getting the result of the Bellman-Ford algorithm.

    Returns:
        result (SinglePathResultViewModel): Result containing list of coordinates
        representing the shortest path from HCMUT to Sheraton Hotel.
    """
    return BellmanFordService.get_shortest_path(adjacency_matrix, nodes, index_hcmut, index_sheraton)

@app.get("/floyd-warshall", tags=["Floyd-Warshall Algorithm"], status_code=status.HTTP_200_OK, response_model=SinglePathResultViewModel)
async def floyd_warshall():
    """
    Endpoint for getting the result of the Floyd-Warshall algorithm.

    Returns:
        result (SinglePathResultViewModel): Result containing list of coordinates
        representing the shortest path from HCMUT to Sheraton Hotel.
    """
    return FloydWarshallService.get_shortest_path(adjacency_matrix, nodes, index_hcmut, index_sheraton)

@app.get("/yen", tags=["Yen Algorithm"], status_code=status.HTTP_200_OK, response_model=MultiplePathsResultViewModel)
async def yen(k: int = Query(ge=1, le=100, default=5)):
    """
    Endpoint for getting the result of the Yen algorithm.

    Parameters:
        k (int): The number of shortest paths to compute, between 1 and 100,
        with a default value of 5.

    Returns:
        result (MultiplePathsResultViewModel): Result containing list of list of
        coordinates representing K shortest paths from HCMUT to Sheraton Hotel.
    """
    return YenService.get_shortest_path(adjacency_matrix, nodes, index_hcmut, index_sheraton, k)