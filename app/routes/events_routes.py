from fastapi import APIRouter,Depends, HTTPException
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.schema import event_schema
from app.services import event_services

event_router = APIRouter(
    prefix = "/event",
    tags = ["Event Routes"]
)

@event_router.get("/")
def CheckHealth():
    return {
        "message": "Events Routes is working"
    }

@event_router.get("/about")
def checkAbout():
    return {
        "message": "Updated Routes"
    }

@event_router.post("/add-event", response_model= event_schema.Eventresponse)
def AddEvent(
    data: event_schema.Eventcreate,
    db: Session = Depends(get_db)
):
    return event_services.create_Event(db, data)

@event_router.get("/getall")
def Get_all(db: Session = Depends(get_db)):
    return event_services.get_all(db)

@event_router.get("/getid/{event_id}")
def Get_by_id(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = event_services.get_by_id(db, event_id)

    if not event:
        return HTTPException(
            status_code = 404,
            detail = "Not Found"
        )
    return event


@event_router.delete("/del/{event_id}")
def Delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = event_services.delete_event(db, event_id)

    if not event:
        return HTTPException(
            status_code = 404,
            detail = "Not Found"
        )
    return {"Message": f"Event deleted: {event_id}"} 


@event_router.put("/update/{event_id}", response_model= event_schema.Eventresponse)
def UpdateEvent(
    event_id = int,
    Event_data =  event_schema.Eventcreate,
    db: Session = Depends(get_db)
):
    event = event_services.Update_event(event_id, Event_data, db)

    if not event:
        return HTTPException(
            status_code = 404,
            detail = "Not Found"
        )
    return event