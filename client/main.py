# client/main.py

from fastapi import FastAPI
from client.routers import queue

app = FastAPI(
    title="Hvalfangst API",
    description="API used to interact with Azure storage queues",
    version="1.0.0"
)

# Register the queue router
app.include_router(queue.router, prefix="/queue", tags=["Endpoints used to interact with our storage queue"])