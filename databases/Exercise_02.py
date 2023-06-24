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
film_category = sqlalchemy.Table("film_category", metadata, autoload_with=engine)
inventory = sqlalchemy.Table("inventory", metadata, autoload_with=engine)
rental = sqlalchemy.Table("rental", metadata, autoload_with=engine)
payment = sqlalchemy.Table("payment", metadata, autoload_with=engine)
"""
#1)
query = sqlalchemy.select(actor).where(actor.columns.first_name.in_(["WILLIAM"]))
result_proxy = connection.execute(query)


#2)

join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id) 
join_statement = join_actor_film_actor.join(film, film.columns.film_id == film_actor.columns.film_id)

query = sqlalchemy.select(film.columns.title, actor.columns.first_name, actor.columns.last_name).select_from(join_statement)


#3) 5) 6)

join_statement_1 = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id) 
join_statement_2 = join_statement_1.join(film, film.columns.film_id == film_actor.columns.film_id)
join_statement_3 = join_statement_2.join(film_category, film_category.columns.film_id == film.columns.film_id)
join_statement_4 = join_statement_3.join(category, category.columns.category_id == film_category.columns.category_id)

query = sqlalchemy.select(actor.columns.first_name, actor.columns.last_name, film.columns.title).where(film.columns.title.in_(["AIRPLANE SIERRA"]))
query = query.select_from(join_statement_4)
query = query.group_by(film.columns.title, actor.columns.first_name, actor.columns.last_name)
query = query.order_by(actor.columns.last_name.asc())

"""
#4)

join_film_film_category = film.join(film_category, film_category.columns.film_id == film.columns.film_id)
join_film_category_category = join_film_film_category.join(category, category.columns.category_id == film_category.columns.category_id)
join_film_inventory = join_film_category_category.join(inventory, inventory.columns.film_id == film.columns.film_id)
join_inventory_rental = join_film_inventory.join(rental, rental.columns.inventory_id == inventory.columns.inventory_id)
join_payment_rental = join_inventory_rental.join(payment, payment.columns.rental_id == rental.columns.rental_id)
join_statement = join_payment_rental

query = sqlalchemy.select(film.columns.title, payment.columns.amount).where(category.columns.name.in_(["Comedy"])).order_by(payment.columns.amount.asc())
query = query.select_from(join_statement)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)
