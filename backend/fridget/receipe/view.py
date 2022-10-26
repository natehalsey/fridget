
from model import Recipe

class RecipeViewer:
    async def create(recipe: Recipe):
        await Recipe.create(recipe)

    def update():
        #does user have permission to?
        pass

    def delete():
        #does user have permission to?
        pass

    def search_by_name():
        pass

    def search_by_category():
        pass

    def search_by_area():
        pass

    def search_by_ingredients():
        pass

    def search_by_ids():
        pass