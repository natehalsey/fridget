

from model import Category, APIResponseModel
from requests import request, RequestException 
from typing import List
from fridget.base.config import Settings

DATABASE_URL = Settings.DATABASE
class CategoryContoller:
    """ 
        Handles gettings with areas from api and db 
    """
    async def load_catagories_from_api(self):
        """
            Returns all recipes catagories
        """

        response = request("GET", 
                "https://themealdb.p.rapidapi.com/list.php", 
                headers=Settings.HEADERS, 
                params={'c': 'list'})


        ## create Category objects from response
        categories = APIResponseModel.parse_raw(response.text)
        print(categories.meals)


        await Category.objects.bulk_create(categories.meals)

  

    async def select_categories(self, patterns: List[str]):
        return await Category.objects.filter(Category.name._in_(patterns)).all()

    async def filter_startwith(self, pattern: str):
        return await Category.objects.filter(Category.name.istartswith(pattern)).all()

    async def filter_contains(self, pattern: str):
         return await Category.objects.filter(Category.name.icontains(pattern)).all()


################################

    async def test(self):
        o = CategoryContoller()
        await o.load_catagories_from_api()
        return await o.filter_startwith("V")
 


