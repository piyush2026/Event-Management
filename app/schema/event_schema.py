from pydantic import BaseModel

class EventCreate(BaseModel):
    event_name: str
    evet_date: str
    event_type: str

class EventResposnse(EventCreate):
    id : int 

    class config:
        from_attributes = True