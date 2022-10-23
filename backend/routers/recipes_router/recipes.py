from fastapi import APIRouter,HTTPException,status,Response
import requests
from . import recipes_utils
from ..db_utils import querys
from ..db_utils.db_proxy import db_proxy
from fastapi.responses import JSONResponse

recipesRoute = APIRouter()


@recipesRoute.get('/recipes/{ingredient_name}',status_code=status.HTTP_200_OK , response_class= JSONResponse)
def recipesByIngredient(ingredient_name , gluten_free = None , dairy_free = None):
    try:
        recipes = recipes_utils.get_recipes(ingredient_name)
        recipes_list = recipes_utils.convert_to_recipe_class(recipes)

        if (not gluten_free) and (not dairy_free):
            return recipes_list

        elif gluten_free and (not dairy_free):
            ingredients_list = recipes_utils.get_gluten_free_ingredients()
            filltered_recipes = recipes_utils.fillter_by_ingredients(recipes_list,ingredients_list)
            return filltered_recipes , len(filltered_recipes) , len(recipes_list)
        
        elif dairy_free and (not gluten_free):
            ingredients_list = recipes_utils.get_dairy_free_ingredients()
            filltered_recipes = recipes_utils.fillter_by_ingredients(recipes_list,ingredients_list)
            return filltered_recipes

        else:
            gluten_free_list = recipes_utils.get_gluten_free_ingredients()
            dairy_free_list = recipes_utils.get_dairy_free_ingredients()
            filltered_gluten_recipes = recipes_utils.fillter_by_ingredients(recipes_list,gluten_free_list)
            filltered_dairy_recipes = recipes_utils.fillter_by_ingredients(filltered_gluten_recipes,dairy_free_list)
            return filltered_dairy_recipes

    except Exception as e:
        return e