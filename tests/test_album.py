from lib.album import Album

"""
id, title, release_year, artist_id

Check that the album class constructs correctly
"""

def test_album_constructs():
    album = Album(1, "Test_Title", 2024, 1)
    assert album.id == 1
    assert album.title == "Test_Title"
    assert album.release_year == 2024
    assert album.artist_id == 1

"""
We can format artists to strings nicely
"""

def test_albums_format_nicely():
    album = Album(1, "Test_Title", 2024, 1)
    assert str(album) == "Album(1, Test_Title, 2024, 1)"

"""
We can compare two identical artists
And have them be equal
"""

def test_albums_are_equal():
    album1 = Album(1, "Test_Title", 2024, 1)
    album2 = Album(1, "Test_Title", 2024, 1)
    assert album1 == album2