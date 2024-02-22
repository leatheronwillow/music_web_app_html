from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
"""
GET /albums
Expected response (200 OK):
Returns list of album titles
"""
def test_get_albums(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Doolittle, Surfer Rosa, Waterloo'

"""
POST /albums
 Parameters: 
   title: Voyage
   release_year: 2022
   artist_id: 2
 Expected response (200 Ok): 
   returns None
   running GET /albums returns 'Doolittle, Surfer Rosa, Voyage' 
"""
def test_post_albums(web_client,db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums', data={'title':'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Album added successfully'
    response = web_client.get('/albums')
    assert response.data.decode('utf-8') == 'Doolittle, Surfer Rosa, Waterloo, Voyage'

"""
POST /albums
 Parameters: none
 Expected response (400 Bad Request): 'Album Details not found'
"""

def test_post_albums_invalid(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Album Details not found'

"""
GET /artists
Expected: List of artists in string form
"""

def test_get_artists(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

"""
POST /artists
Parameters:
  name: Wild nothing
  genre: Indie
=> 200 Ok
GET /artists reflects new artist in list of artists
"""
def test_post_artist(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""
    response = web_client.get('/artists')
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'

def test_post_artists_invalid(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Artist Details not found'