from requests import request, RequestException 
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from ..base.config import Settings
from uuid import uuid4


router = APIRouter(
    prefix = ""
)
headers = Settings.HEADERS

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
