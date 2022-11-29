import ormar
import databases
import sqlalchemy
from typing import Optional
from pydantic import json
from .config import Settings

DATABASE_URL = Settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class Area(ormar.Model):
    class Meta(BaseMeta):
        tablename="areas"
    
    name: str = ormar.String(max_length=30, unique=True, primary_key=True)

class Category(ormar.Model):
    class Meta(BaseMeta):
        tablename="categories"
    
    name: str = ormar.String(max_length=50, unique=True, primary_key=True)
    
class Ingredient(ormar.Model):
    class Meta(BaseMeta):
        tablenmae="ingredients"
    
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=500, unique=True)
    description: Optional[str] = ormar.Text(nullable=True)
    type: Optional[str] = ormar.String(max_length=50, nullable=True)

class Recipe(ormar.Model):     

    class Meta(BaseMeta):
        tablename="recipes"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    category: Category = ormar.ForeignKey(Category)
    area: Area = ormar.ForeignKey(Area)
    instructions: Optional[str] = ormar.Text(nullable=True)
    ingredients: list[Ingredient] = ormar.ManyToMany(Ingredient, related_name="recipes")
    ingredients_measurements: json = ormar.JSON(nullable=True)
    image_url: Optional[str] = ormar.String(max_length=200, nullable=True)
    source: Optional[str] = ormar.String(max_length=500, nullable=True)
 

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename="users"
        
    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=200, unique=True)
    email: str = ormar.String(max_length=200, unique=True)
    hashed_password: str = ormar.String(max_length=200)
    ingredients: list[Ingredient] = ormar.ManyToMany(Ingredient)

class UserCreatedRecipe(ormar.Model):
    class Meta(BaseMeta):
        tablename="users_created_recipes"
        
    id: int = ormar.Integer(primary_key=True)    
    user: User = ormar.ForeignKey(User, related_name="created_recipes")
    recipe: Recipe = ormar.ForeignKey(Recipe, unique=True, skip_reverse=True)  
 
class UserSavedRecipe(ormar.Model):
    class Meta(BaseMeta):
        tablename="users_saved_recipes"
    
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="saved_recipes")
    recipe: Recipe = ormar.ForeignKey(Recipe, unique=True, skip_reverse=True)  