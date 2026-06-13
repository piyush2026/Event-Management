from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Event(Base):
    __tablename__ = "event"

    id= Column(Integer, primary_key= True, index= True)
    event_name = Column(String)
    event_date = Column(String)
    event_type = Column(String)
