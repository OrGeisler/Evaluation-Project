import pymysql
import json
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def table_insert(ingredients_list , table ):
    for ingredient in ingredients_list:
        try:
            with connection.cursor() as cursor:
                query = f'INSERT into {table} (name) values ("{ingredient}")'
                cursor.execute(query)
                connection.commit()
        except:
            print("Error")


dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]

table_insert(dairy_ingredients,'dairy_ingredients')
table_insert(gluten_ingredients,'gluten_ingredients')