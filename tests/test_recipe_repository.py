from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
Test the method #all() returns all recipes
"""
def test_returns_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_repository = RecipeRepository(db_connection)
    recipes = recipe_repository.all()

    assert recipes == [
        Recipe(1, 'Fried rice', 10, 3),
        Recipe(2, 'Butter chicken', 35, 4),
        Recipe(3, 'Easy quiche', 45, 5),
        Recipe(4, 'Steak and onions', 25, 5),
        Recipe(5, 'Lasagne', 75, 4)
    ]

"""
Test the method find returns derired recipe
"""
def test_find_returns_wanted_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_repository = RecipeRepository(db_connection)

    found_recipe = recipe_repository.find(2)
    assert found_recipe == Recipe(2, 'Butter chicken', 35, 4)