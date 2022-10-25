from requests import request, RequestException 
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from .schema import Users
from uuid import uuid4


router = APIRouter(
    prefix = ""
)

headers = {
    "X-RapidAPI-Key": "eb35fcf224msh909175e8c268c99p18336bjsn1e11ec2eeddf",
    "X-RapidAPI-Host": "themealdb.p.rapidapi.com"
}

html_content = """<h3>Endpoints</h3>
    <p>See <a href=https://rapidapi.com/thecocktaildb/api/themealdb/>The meal DB API Docs</a><p>
    <h4>1. Filter</h4>
    <ul>
        <li>filter_by_ingredient(ingred: str) <a href=/filter_by_ingredient/?ingred=chicken_breast>/filter_by_ingredient/?ingred=chicken_breast</a></li>
        <li>filter_by_category(cat: str) <a href=/filter_by_category/?cat=seafood>/filter_by_category/?cat=seafood</a></li>
        <li>filter_by_area(area: str) <a href=/filter_by_area/?area=Canadian>/filter_by_area/?area=Canadian</a></li>
    </ul>
    <p></p>

    <h4>2. Search</h4>
    <ul>
        <li>search_by_name(name: str) <a href=/search_by_name/?name&Arrabiata>/search_by_name/?name=Arrabiata</a></li>
        <li>search_by_first_letter(ltr: str) <a href=search_by_first_letter/?ltr=a>search_by_first_letter/?ltr=a</li>
        <li>search_by_id(id: int)<a href=/search_by_id/?id=52772>/lookup/?id=52772</a></li>
        <li>random_recipe()<a href=/random_recipe>/random_recipe</a></li>
    </ul>

    <h4>4. List</h4>
    <ul>
        <li>list_all_ingredients() <a href=/list_all_ingredients>/list_all_ingredients</a></li>
        <li>list_all_areas() <a href=/list_all_areas>/list_all_areas</a></li>
        <li>list_all_catagories() <a href=/list_all_catagories>/list_all_catagories</a></li>
    </ul>
    """

@router.get('/')
def home():
    """
    Returns API home page
    """
    return HTMLResponse(content=html_content, status_code=200)

## Filter Endpoints - API    

@router.get('/filter_by_ingredient')
def filter_by_ingredient(ingred: str):
    """ 
    Returns recipes that have 'ingred' as ingredient. Can be multiple ingredients"
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/filter.php", 
                headers=headers, 
                params={'i': ingred})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/filter_by_category')
def filter_by_category(cat: str):
    """
    Returns recipes are in category 'cat'
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/filter.php", 
                headers=headers, 
                params={'c': cat})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/filter_by_area')
def filter_by_area(area: str):
    """
    Returns recipes are in area 'area'
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/filter.php", 
                headers=headers, 
                params={'a': area})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

## Search Endpoints - API

@router.get('/search_by_name')
def search_by_name(name: str):
    """
    Returns recipes with name matching 'name'
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/search.php", 
                headers=headers, 
                params={'s': name})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/search_by_first_letter')
def search_by_first_letter(ltr: str):
    """
    Returns recipes with first letter of name matching 'ltr'
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/search.php", 
                headers=headers, 
                params={'f': ltr})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/search_by_id')
def search_by_id(id: int):
    """
    Returns recipes with id matching 'id'
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/search.php", 
                headers=headers, 
                params={'i': id})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/random_recipe')
def random_recipe():
    """
    Returns random recipe
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/random.php", 
                headers=headers,)

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

## List Endpoints - API

@router.get('/list_all_catagories')
def list_all_catagories():
    """
    Returns all recipes catagories
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/list.php", 
                headers=headers, 
                params={'c': 'list'})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/list_all_areas')
def list_all_areas():
    """
    Returns all recipes areas
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/list.php", 
                headers=headers, 
                params={'a': 'list'})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))

@router.get('/list_all_ingredients')
def list_all_ingredients():
    """
    Returns all recipes ingredients
    """

    try:
        response = request("GET", 
                "https://themealdb.p.rapidapi.com/list.php", 
                headers=headers, 
                params={'i': 'list'})

        return response.json()

    except RequestException as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))


## User Endpoints - DB
#
@router.post('/new_user')
async def new_user(user: Users):
    print(user)
    # user.password = hash(user.password) can this be add at ORM/DB level?
    await user.save()
    return HTMLResponse(content="<h3>OK</h3>", status_code=200)

@router.post('/login')
async def login(username: str, password: str ):
    return await Users.objects.get(username=username, hashed_password=password)