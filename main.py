from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoices, BandCreate, Band, Album
from typing import Annotated
from sqlmodel import Session, select
import logging
# from contextlib import asynccontextmanager  # not needed anymore
from db import init_db, get_session


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# # not needed because of alembic implementation
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     init_db()
#     yield

# app = FastAPI(lifespan=lifespan)

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

# @app.get("/")
# async def index() -> dict[str, str]:
#     return {"message": "Hello World"}


# @app.get("/about")
# async def about() -> str:
#     return "Nothing to see here"

# @app.get("/bands")
# async def bands(
#     genre: GenreURLChoices | None = None,
#     q: Annotated[
#         str | None,
#         Query(max_length=10)
#     ] = None,
#     session: Session = Depends(get_session)
# ) -> list[Band]:
#     query = select(Band)
#     if genre:
#         query = query.where(Band.genre == genre.value)
#     if q:
#         query = query.where(Band.name.contains(q))
#     return session.exec(query).all()


@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[
        str | None,
        Query(max_length=10)
    ] = None,
    session: Session = Depends(get_session)
) -> list[Band]:
    band_list = session.exec(select(Band)).all()
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
        logger.info("Fetching all bands")

    return band_list


@app.get("/bands/{band_id}")
async def band(
    # add Annotated title for documentation
    band_id: Annotated[int, Path(title='The band ID')],
    session: Session = Depends(get_session)
) ->  Band:
    band = session.get(Band, band_id)
    logger.info(f"Fetching band with id: {band_id}")
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band


# @app.get("/bands/genre/{genre}")
# async def bands_by_genre(genre: GenreURLChoices) -> list[dict]:
#     logger.info(f"Fetching bands with genre: {genre}")
#     return [band for band in BANDS if band['genre'].lower() == genre.value]

@app.post("/bands")
async def create_band(
    band_data: BandCreate,
    session: Session = Depends(get_session)
) -> Band:
    logger.info(f"Creating band: {band_data}")
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)
    
    if band_data.albums:
        for album in band_data.albums:
            album_obj = Album(
                title = album.title,
                release_date = album.release_date,
                band = band
            )
            session.add(album_obj)
    
    session.commit()
    session.refresh(band)
    return band
    