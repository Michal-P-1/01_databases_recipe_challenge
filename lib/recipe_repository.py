from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, db_connection):
        self.connection = db_connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            recipe = Recipe(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(recipe)
        return recipes
    
    def find(self, recipe_id):
        rows = self.connection.execute("SELECT * FROM recipes WHERE id = %s", [recipe_id])
        row = rows[0]
        return Recipe(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])