import ormar
from random import randint
from fastapi import Response
from collections import Counter
from fridget.base.schema import (
    Area,
    Category,
    Ingredient,
    Recipe,
    User,
    UserCreatedRecipe,
    Ingredient
)
from fridget.recipes.models import RecipeModel, IngredientMeasurementModel


# recipe controller controls the recipe objects in the db
class RecipeController:

    async def create_recipe(self, recipe_model: RecipeModel, current_user: User) -> None:
        """
        It takes the inputted recipe model, and create a recipe object, and then create a link between the
        user and the recipe

        :param recipe_model: RecipeModel
        :type recipe_model: RecipeModel
        :param current_user: User = the user who is currently logged in
        :type current_user: User
        """

        area, _ = await Area.objects.get_or_create(
            name=recipe_model.area.name
        )

        category, _ = await Category.objects.get_or_create(
            name=recipe_model.category.name
        )

        recipe = await Recipe.objects.create(
            name=recipe_model.name,
            category=category,
            area=area,
            instructions=recipe_model.instructions,
            ingredients_measurements=recipe_model.dict()[
                "ingredients_measurements"],
            image_url=recipe_model.image_url,
            source=recipe_model.source,
        )
        # add a link between user and created recipe
        await UserCreatedRecipe.objects.create(
            user=current_user,
            recipe=recipe
        )

        # we need to take the inputted json of the ingredients_measurments and turn it into data that we can
        # usefully retain for further use
        ingredients_measurements: list[IngredientMeasurementModel] = recipe_model.ingredients_measurements
        for ingredient_measurement in ingredients_measurements:

            ingredient, _ = await Ingredient.objects.get_or_create(
                name=ingredient_measurement.ingredient
            )
            await recipe.ingredients.add(ingredient)

    async def get_recipes_by_name(self, name: str) -> list[Recipe]:
        """
        "Get all recipes whose name contains the given string."

        :param name: str
        :type name: str
        :return: A list of Recipe objects
        """
        return await Recipe.objects.filter(
            name__icontains=name
        ).all()

    async def get_recipe_by_id(self, id: int) -> Recipe:
        """
        Returns a recipe with the given id, or a 404 if it doesn't exist

        :param id: int - the id of the recipe we want to get
        :type id: int
        :return: A recipe object
        """
        try:
            return await Recipe.objects.get(
                id=id
            )
        except ormar.NoMatch as e:
            return Response(status_code=404, detail="Not found")

    async def get_recipes_by_random(self, n: int) -> Recipe:
        """
        "Get a random offset, then get n recipes starting from that offset."

        :param n: int - The number of recipes to return
        :type n: int
        :return: A list of recipes
        """
        random_offset = randint(0, await Recipe.objects.count() - n)
        return await Recipe.objects.offset(random_offset).limit(n).all()

    async def get_recipes_by_ingredients(self, input_ingredients: list[str]) -> list[RecipeModel]:
        """
        We get all the recipes that have any of the ingredients in the passed list

        :param input_ingredients: list[str]
        :type input_ingredients: list[str]
        :return: A list of RecipeModel objects
        """
        # the problem is that our ingredients are in the database case sensitive
        # ham and HAM could be connected to totally different recipes.

        # if this wasn't the case, we could do a simple name__in = input_ingredients
        # unfortunately we have to do this instead, adding a lot of complexity.
        recipes = [
            recipes for ingredient_name in input_ingredients for recipe in
            await Ingredient.objects.select_related("recipes").filter(
                name__iexact=ingredient_name
            ).all()
            for recipes in recipe.recipes
        ]

        # now we have a list of recipes, with some duplicates

        # count up the recipe ids
        counts = Counter([recipe.id for recipe in recipes])

        # sort by most count (because of duplicates)
        sorted_recipes = sorted(
            recipes,
            key=lambda recipe: counts[recipe.id],
            reverse=True
        )

        # the recipes with the most duplicates are exactly the recipes that have the most ingredients in the passed list
        return sorted_recipes
