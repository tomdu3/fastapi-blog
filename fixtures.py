from datetime import datetime
from sqlmodel import Session
from db import engine
from models import Band, Album

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

def create_bands():
    with Session(engine) as session:
        for band_data in BANDS:
            albums = band_data.pop('albums', [])
            band = Band(**band_data)
            for album_data in albums:
                release_date_str = album_data.pop('release_date')
                release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
                album = Album(**album_data, release_date=release_date, band=band)
                session.add(album)
            session.add(band)
        session.commit()

if __name__ == "__main__":
    create_bands()