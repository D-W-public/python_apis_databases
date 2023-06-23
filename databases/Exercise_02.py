'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

1) Select all the actors with the first name of your choice

2) Select all the actors and the films they have been in

3) Select all the actors that have appeared in a category of a comedy of your choice

4) Select all the comedic films and sort them by rental rate

5) Using one of the statements above, add a GROUP BY statement of your choice

6) Using one of the statements above, add a ORDER BY statement of your choice

'''
import sqlalchemy
import os
from pprint import pprint
sql_sakila_login = os.environ['sql_sakila']

#Conection Set-up for DB
engine = sqlalchemy.create_engine(sql_sakila_login)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#Tables
film = sqlalchemy.Table("film", metadata, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload_with=engine)
actor = sqlalchemy.Table("actor", metadata,autoload_with=engine)
film_actor = sqlalchemy.Table("film_actor", metadata, autoload_with=engine)


#1)
query = sqlalchemy.select(actor).where(actor.columns.first_name.in_(["WILLIAM"]))
#result_proxy = connection.execute(query)
""""
2)
join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id) 
join_statement = join_actor_film_actor.join(film.columns.film_id == film_actor.columns.film_id)
 
query = sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name].select_from(join_statement))
"""
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)