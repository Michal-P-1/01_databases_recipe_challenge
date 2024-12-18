from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# Retrieve all recipes
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
for artist in artists:
    print(artist)

for recipe in recipes:
    print(recipe)

