from fastapi import APIRouter, Query
from starlette import status

from models.result import MultiplePathsResultViewModel
from services.utils import adjacency_matrix, nodes, index_hcmut, index_sheraton
from services import yen as YenService

router = APIRouter(prefix="/yen", tags=["Yen Algorithm"])

@router.get("", status_code=status.HTTP_200_OK, response_model=MultiplePathsResultViewModel)
async def yen(
    source_vertex: int = Query(ge=0, default=index_hcmut),
    destination_vertex: int = Query(ge=0, default=index_sheraton),
    k: int = Query(ge=1, le=100, default=5)
):
    """
    Endpoint for getting the result of the Yen algorithm.

    Parameters:
        source_vertex: Index of the source vertex
        destination_vertex: Index of the destination vertex
        k (int): The number of shortest paths to compute, between 1 and 100

    Returns:
        result (MultiplePathsResultViewModel): Result containing list of list of
        coordinates representing K shortest paths from source vertex to destination vertex.
    """
    return YenService.get_shortest_path(adjacency_matrix, nodes, source_vertex, destination_vertex, k)