from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date

class GenreURLChoices(str, Enum):
    rock = "rock"
    grunge = "grunge"
    alternative = "alternative"
    progressive_rock = "progressive rock"


class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: GenreURLChoices
    albums: list[Album] = []
    
    
    @field_validator('genre', mode='before')
    def to_lowercase_strip(cls, v):
        if isinstance(v, str):
            return v.lower().strip()
        return v

class BandCreate(BandBase):
    pass

class BandWithID(BandBase):
    id: int
    pass