sql_insert_type =    """
                           INSERT IGNORE into type (name) 
                           values (%s)
                           """
sql_get_pokemon_id =    """
                        SELECT p.id
                        FROM pokemon p
                        WHERE p.name = %s
                        """

sql_delete_pokemon_of_trainer = """
                                DELETE FROM owned_by 
                                WHERE trainer_name = %s
                                AND pokemon_id = %s
                                """

