from fastapi import FastAPI
from app.routes.events_routes import event_router

app = FastAPI()
app.include_router(event_router)

@app.get("/")
def CheckHealth():
    return {
        "message":"FastAPI is Working "
    }
