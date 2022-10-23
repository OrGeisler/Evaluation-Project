import requests

def test_get_recipe():
    response = requests.get(f'http://127.0.0.1:8001/recipes/cheese')
    assert isinstance(response,requests.models.Response)==True
    assert response.status_code==200

def test_get_recipe_gluten_free():
    response = requests.get(f'http://127.0.0.1:8001/recipes/cheese?gluten_free=True')
    assert isinstance(response,requests.models.Response)==True
    assert response.status_code==200

def test_get_recipe_dairy_free():
    response = requests.get(f'http://127.0.0.1:8001/recipes/cheese?dairy_free=True')
    assert isinstance(response,requests.models.Response)==True
    assert response.status_code==200

def test_get_recipe_dairy_gluten_free():
    response = requests.get(f'http://127.0.0.1:8001/recipes/cheese?dairy_free=True&gluten_free=True')
    assert isinstance(response,requests.models.Response)==True
    assert response.status_code==200