import json
from requests import request
from fridget.base.config import Settings
from fridget.base.schema import RecipeIngredientMeasurement, Recipe, Ingredient, Area, Category, Measurement, RecipeIngredientMeasurement

async def download_db():
    # get categories
    category_response = request(
        "GET",
        "http://www.themealdb.com/api/json/v1/1/list.php?c=list?",
        headers=Settings.HEADERS 

    )
    category_response = category_response.json()
    meals = category_response["meals"]
    for meal in meals:
        await Category.objects.get_or_create(
            name=meal["strCategory"],
        )
    print(await Category.objects.all())

    # get areas
    area_response = request(
        "GET",
        "http://www.themealdb.com/api/json/v1/1/list.php?a=list?",
        headers=Settings.HEADERS 

    )
    area_response = area_response.json()
    meals = area_response["meals"]
    for meal in meals:
        await Area.objects.get_or_create(
            name=meal["strArea"],
        )
    print(await Area.objects.all())
    
    # get ingredients
    ingredient_response = request(
        "GET",
        "http://www.themealdb.com/api/json/v1/1/list.php?i=list",
        headers=Settings.HEADERS 

    )
    ingredient_response = ingredient_response.json()
    meals = ingredient_response["meals"]
    for meal in meals:
        await Ingredient.objects.get_or_create(
            name=meal["strIngredient"],
            description=meal["strDescription"],
            type=meal["strType"]
        )
    print(await Ingredient.objects.all())
    
    response = request(
        "GET", 
        "https://themealdb.p.rapidapi.com/search.php", 
        headers=Settings.HEADERS, 
        params={'s': ''}
    )
    
    # get recipes and ingredients and the linked tables
    response = response.json()
    meals = response["meals"]
    for meal in meals:
        ingredients_measurements = []
        category = await Category.objects.get_or_create(
            name=meal["strCategory"]
        )
        area = await Area.objects.get_or_create(
            name=meal["strArea"]
        )
        recipe =await Recipe.objects.get_or_create(
            name=meal["strMeal"],
            category=category[0],
            area=area[0],
            instructions=meal["strInstructions"],
            image_url=meal["strMealThumb"],
            source=meal["strSource"]
        )
        for i in range(1,20):
            name=meal["strIngredient"+str(i)]
            measurement=meal["strMeasure"+str(i)]
            
            if name != None and name != "" and measurement != None and measurement != "":
            
                ingredient = await Ingredient.objects.get_or_create(
                    name=name
                )
                measurement = await Measurement.objects.get_or_create(
                    measurement=measurement
                )
                ingredient=ingredient[0]
                measurement=measurement[0]

                ingredients_measurements.append({"ingredient": ingredient.name, "measurement": measurement.measurement})                

                await RecipeIngredientMeasurement.objects.get_or_create(
                    ingredient=ingredient.id,
                    measurement=measurement.id,
                    recipe=recipe[0].id
                )
                
        await recipe[0].update(
            ingredients_measurements=json.dumps(ingredients_measurements)
        )
    print(await RecipeIngredientMeasurement.objects.all())
    return await Recipe.objects.all()