from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import SQLModel, Field, Relationship
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


class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int | None = Field(default=None, foreign_key='band.id')


class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: 'Band' = Relationship(back_populates='albums')
    
class BandBase(SQLModel):
    name: str
    genre: GenreChoices

class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None

    # Title case the genre and strip whitespace
    @field_validator('genre', mode='before')
    def title_case_genre(cls, v):
        if isinstance(v, str):
            return v.title().strip()

class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates='band')