from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date

class GenreURLChoices(str, Enum):
    rock = "rock"
    grunge = "grunge"
    alternative = "alternative"
    progressive_rock = "progressive rock"

class GenreChoices(str, Enum):
    rock = "Rock"
    grunge = "Grunge"
    alternative = "Alternative"
    progressive_rock = "Progressive Rock"

class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []

class BandCreate(BandBase):
    # Title case the genre and strip whitespace
    @field_validator('genre', mode='before')
    def title_case_genre(cls, v):
        if isinstance(v, str):
            return v.title().strip()

class BandWithID(BandBase):
    id: int