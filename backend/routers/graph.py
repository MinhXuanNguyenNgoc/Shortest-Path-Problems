from fastapi import APIRouter, Query
from starlette import status

from models.result import GraphResultViewModel
from services.utils import adjacency_matrix, nodes, index_hcmut, index_sheraton
from services import graph as GraphService

router = APIRouter(prefix="/graph", tags=["Graph"])

@router.get("", status_code=status.HTTP_200_OK, response_model=GraphResultViewModel)
async def get_graph():
    """
    Endpoint for getting the graph of points between HCMUT and Sheraton Hotel.

    Returns:
        result (GraphResultViewModel): Result containing list of coordinates
        and edges of the points between HCMUT and Sheraton Hotel.
    """
    return GraphService.get_graph()