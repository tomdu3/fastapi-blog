from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(str, Enum):
    rock = "rock"
    grunge = "grunge"
    alternative = "alternative"
    progressive_rock = "progressive rock"


class Band(BaseModel):
    # {'id': 1, 'name': 'The Beatles', 'genre': 'Rock'},
    id: int
    name: str
    genre: GenreURLChoices
    
    
