'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
import os
from pprint import pprint
sql_sakila_login = os.environ['sql_sakila']

engine = sqlalchemy.create_engine(sql_sakila_login)
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table("film", metadata, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload_with=engine)

pprint(repr(metadata.tables["film"]))
pprint(repr(metadata.tables["category"]))