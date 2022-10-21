import pymysql
import json
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# def pokemon_insert():
#     file = open('poke_data.json')
#     data = json.load(file)
#     for pokemon in data:
#         try:
#             with connection.cursor() as cursor:
#                 query = f'INSERT into pokemon (name,height,weight) values ("{pokemon["name"]}","{pokemon["height"]}",{pokemon["weight"]})'
#                 cursor.execute(query)
#                 connection.commit()
#         except:
#             print("Error")
#     file.close()