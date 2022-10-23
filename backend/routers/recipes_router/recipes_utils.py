from fastapi import HTTPException
import requests
from ..db_utils import querys
from ..db_utils.db_proxy import db_proxy
from dataclasses import dataclass

db = db_proxy()

@dataclass
class Recipe():
    ingredients:list
    title:str
    thumbnail:str
    href:str



def get_recipes(ingredient_name):
    try:
        recipes= requests.get(f'https://recipes-goodness.herokuapp.com/recipes/{ingredient_name}').json()['results']
        return recipes
    except:
        raise HTTPException(status_code=404, detail="Error, Cant find the recipes in the external API")

def convert_to_recipe_class(recipes):
    try:
        recipes_list = []
        for recipe in recipes:
            recipe_class = Recipe(recipe["ingredients"],recipe["title"],recipe["thumbnail"],recipe["href"])
            recipes_list.append(recipe_class)
        return recipes_list
    except Exception as e:
        return e

def get_gluten_free_ingredients():
    ingredients = db.execute_select_all_query(querys.sql_get_gluten_free_ingredients)
    ingredients_list =  []
    for ingredient in ingredients:
        ingredients_list.append(ingredient['name'])
    return ingredients_list

def get_dairy_free_ingredients():
    ingredients = db.execute_select_all_query(querys.sql_get_dairy_free_ingredients)
    ingredients_list =  []
    for ingredient in ingredients:
        ingredients_list.append(ingredient['name'])
    return ingredients_list

def check_ingredient(recipe_ingredients,ingredients_list):
    for i in recipe_ingredients:
        if i.capitalize() in ingredients_list:
            return False
    return True

def fillter_by_ingredients(recipes_list,ingredients_list):

    filltered_recipes = list(filter(lambda recipe: check_ingredient(recipe.ingredients,ingredients_list)  ,recipes_list))
    return filltered_recipes