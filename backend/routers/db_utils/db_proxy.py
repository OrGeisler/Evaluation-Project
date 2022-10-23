import pymysql

class db_proxy:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                                                host='localhost',
                                                user='root',
                                                password="",
                                                db="recipes_app",
                                                charset="utf8",
                                                cursorclass=pymysql.cursors.DictCursor
                                            )
        except pymysql.Error as e:
            print("Error while connecting to MySQL", e)
            
    def execute_select_all_query(self, sql_query, params = None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params) if params else cursor.execute(sql_query)
                result = cursor.fetchall()
                print(f'selected {result} successfully')
                return result
        except pymysql.Error as e:
            print("Failed to select all from MySQL table {}".format(e))