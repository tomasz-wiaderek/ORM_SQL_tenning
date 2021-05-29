from ORM.create_db import engine, Director
from sqlalchemy import insert


connection = engine.connect()

directors = [
    {'name': 'Frank', 'surname': 'Darabont', 'rating': 7},
    {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8},
    {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10},
    {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9},
    {'name': 'David', 'surname': 'Fincher', 'rating': 7}
]

insert_query = insert(Director)
connection.execute(insert_query, directors)
connection.close()
