from fastapi import APIRouter, Query
from starlette import status

from models.result import SinglePathResultViewModel
from services.utils import adjacency_matrix, nodes, index_hcmut, index_sheraton
from services import floyd_warshall as FloydWarshallService

router = APIRouter(prefix="/floyd-warshall", tags=["Floyd-Warshall Algorithm"])

@router.get("", status_code=status.HTTP_200_OK, response_model=SinglePathResultViewModel)
async def floyd_warshall(
    source_vertex: int = Query(ge=0, default=index_hcmut),
    destination_vertex: int = Query(ge=0, default=index_sheraton)
):
    """
    Endpoint for getting the result of the Floyd-Warshall algorithm.

    Parameters:
        source_vertex: Index of the source vertex
        destination_vertex: Index of the destination vertex

    Returns:
        result (SinglePathResultViewModel): Result containing list of coordinates
        representing the shortest path from source vertex to destination vertex.
    """
    return FloydWarshallService.get_shortest_path(adjacency_matrix, nodes, source_vertex, destination_vertex)