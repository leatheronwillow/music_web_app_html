import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repo import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repo import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    album_titles = [album.title for album in albums]
    return ', '.join(album_titles)

@app.route('/albums', methods=['POST'])
def post_albums():
    form = request.form
    if 'title' not in form or 'release_year' not in form or 'artist_id' not in form:
        return 'Album Details not found', 400 
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.create(Album(None, request.form['title'], request.form['release_year'], request.form['artist_id']))
    return 'Album added successfully'

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = [artist.name for artist in artists]
    return ', '.join(artist_names)

@app.route('/artists', methods=['POST'])
def create_artist():
    form = request.form
    if 'name' not in form or 'genre' not in form:
        return 'Artist Details not found', 400 
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.create(Artist(None, request.form['name'], request.form['genre']))
    return ''


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
