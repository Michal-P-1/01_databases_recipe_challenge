from lib.recipe import Recipe

"""
Constructs with id, recipe_name, cooking_time, rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Spaghetti bolognese", 30, 4)
    assert recipe.id == 1
    assert recipe.recipe_name == "Spaghetti bolognese"
    assert recipe.cooking_time == 30
    assert recipe.rating == 4

"""
Test that two same objects(same parameters)
when compared 
are equal
"""
def test_objects_with_same_parameters_equal():
    recipe_1 = Recipe(1, "Spaghetti bolognese", 30, 4)
    recipe_2 = Recipe(1, "Spaghetti bolognese", 30, 4)
    assert recipe_1 == recipe_2

"""
Test object string format
"""
def test_object_string_format():
    recipe = Recipe(1, "Spaghetti bolognese", 30, 4)
    assert str(recipe) == "Recipe(1, Spaghetti bolognese, 30, 4)"