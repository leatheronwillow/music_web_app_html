from lib.album_repo import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository #all
We get a list of Artit objects relfecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums[0:3] == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, "Waterloo", 1974, 2)

"""
When we call AlbumRepository#create
We get a new Album object 
"""

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "American Idiot", 2000, 3))
    albums = repository.all()
    assert albums[-1] == Album(4, "American Idiot", 2000, 3)

"""
Call AlbumRepository#Delete to delete an album
"""

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete(1)
    albums = repository.all()
    assert albums[0:2] == [
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2)
    ]

