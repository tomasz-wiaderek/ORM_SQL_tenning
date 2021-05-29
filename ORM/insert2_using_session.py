from sqlalchemy.orm import sessionmaker
from ORM.create_db import engine, Movie

movies = [
    {'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8},
    {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6},
    {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7},
    {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6},
    {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9},
    {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8},
    {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9},
    {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8},
    {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10},
    {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7},
    {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5},
    {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8},
    {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}
]

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([Movie(**movie) for movie in movies])
session.commit()
