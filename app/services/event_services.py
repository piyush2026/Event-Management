from app.models.events_model import Event
from sqlalchemy.orm import Session
from app.schema import event_schema

def create_Event(db: Session, Event_data):
    new_event = Event(
        event_name = Event_data.event_name,
        event_date = Event_data.event_date,
        event_type = Event_data.event_type
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event

def get_all(db: Session):
    return db.query(Event).all()



def get_by_id(db: Session, event_id:int):
    return db.query(Event).filter(Event.id == event_id).first()


def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if event:
        db.delete(event)
        db.commit()

    return event

def Update_event(
        event_id: int,
        Event_data: event_schema.Eventcreate,
        db: Session
):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        return None
    
    for key, value in Event_data.model_dump().items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)

    return event