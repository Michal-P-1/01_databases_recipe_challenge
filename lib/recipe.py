class Recipe:
    def __init__(self, id, recipe_name, cooking_time, rating):
        self.id = id
        self.recipe_name = recipe_name
        self.cooking_time = cooking_time
        self.rating = rating
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.recipe_name}, {self.cooking_time}, {self.rating })"