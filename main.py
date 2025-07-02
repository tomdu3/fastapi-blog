from fastapi import FastAPI, HTTPException, Path, Query
from typing import Annotated
import logging
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()


BANDS = [
    {'id': 1, 'name': 'The Beatles', 'genre': 'Rock'},
    {'id': 2, 'name': 'Nirvana', 'genre': 'Grunge', 'albums': [
        {'title': 'Nevermind', 'release_date': '1991-10-14'},
        {'title': 'In Utero', 'release_date': '1993-03-07'},
        ]},
    {'id': 3, 'name': 'The Rolling Stones', 'genre': 'Rock'},
    {'id': 4, 'name': 'Radiohead', 'genre': 'Alternative'},
    {'id': 5, 'name': 'Led Zeppelin', 'genre': 'Rock'},
    {'id': 6, 'name': 'Pink Floyd', 'genre': 'Progressive Rock'},
    {'id': 7, 'name': 'Queen', 'genre': 'Rock'},
    {'id': 8, 'name': 'The Who', 'genre': 'Rock'},
    {'id': 9, 'name': 'U2', 'genre': 'Rock'},
    {'id': 10, 'name': 'AC/DC', 'genre': 'Rock'},
]

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/about")
async def about() -> str:
    return "Nothing to see here"


@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[
        str | None,
        Query(max_length=10)
    ] = None
) -> list[BandWithID]:
    band_list = [BandWithID(**band) for band in BANDS]

    filtered = False # Add a flag to track if any filtering happened

    if genre:
        logger.info(f"Fetching bands with genre: {genre}")
        band_list = [
            band for band in band_list if band.genre.value.lower() == genre.value
        ]
        filtered = True

    if q:
        logger.info(f"Fetching bands with query: {q}")
        band_list = [
            band for band in band_list if q.lower() in band.name.lower()
        ]
        filtered = True

    if not filtered: # Log "Fetching all bands" only if no filtering occurred
        logger.info(f"Fetching all bands")

    return band_list


@app.get("/bands/{band_id}")
async def band(
    band_id: Annotated[
        int,
        Path(title='The band ID')  # add Annotated title for documentation
        ]) ->  BandWithID:
    logger.info(f"Fetching band with id: {band_id}")
    band_found = next(
        (BandWithID(**band) for band in BANDS if band['id'] == band_id),
        None
        )
    if band_found is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band_found


@app.get("/bands/genre/{genre}")
async def bands_by_genre(genre: GenreURLChoices) -> list[dict]:
    logger.info(f"Fetching bands with genre: {genre}")
    return [band for band in BANDS if band['genre'].lower() == genre.value]

@app.post("/bands")
async def create_band(band_data: BandCreate) -> BandWithID:
    logger.info(f"Creating band: {band_data}")
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
    