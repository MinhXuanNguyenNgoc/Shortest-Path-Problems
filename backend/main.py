"""API"""

from fastapi import FastAPI
from starlette import status

from routers import bellman_ford, dijkstra, floyd_warshall, yen, graph

app = FastAPI()

app.include_router(graph.router)
app.include_router(bellman_ford.router)
app.include_router(dijkstra.router)
app.include_router(floyd_warshall.router)
app.include_router(yen.router)


@app.get("/", tags=["Health Check"], status_code=status.HTTP_200_OK, response_model=str)
async def health_check():
    """
    Endpoint for checking the health status of the API service.

    Returns:
        str: A message indicating that the API service is up and running.

    """
    return "API Service is up and running!"