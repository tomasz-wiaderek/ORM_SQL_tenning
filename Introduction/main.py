import MySQLdb


db_connection = MySQLdb.connect(host="localhost", user="root", passwd="Programer2021!", db="cinematic")

create_db_query = """CREATE DATABASE IF NOT EXISTS cinematic;"""

create_tables_query = """CREATE TABLE IF NOT EXISTS directors(
          director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
          name VARCHAR(30) NOT NULL, 
          surname VARCHAR(30) NOT NULL, 
          rating INT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS  movies(
          movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
          title VARCHAR(30) NOT NULL, 
          year INT UNSIGNED NOT NULL, 
          category VARCHAR(30) NOT NULL, 
          director_id INT NOT NULL, 
          rating INT NOT NULL, 
          FOREIGN KEY (director_id) REFERENCES directors(director_id)
        );
        """

insert_directors_query = """INSERT INTO directors (name, surname, rating) VALUES(%s, %s, %s)"""
insert_movies_query = """INSERT INTO movies (title, year, category, director_id, rating) VALUES(%s, %s, %s, %s, %s)"""
directors = [('Frank', 'Darabont', 7), ('Francis Ford', 'Coppola', 8), ('Quentin', 'Tarantino', 10),
             ('Christopher', 'Nolan', 9), ('David', 'Fincher', 7)]
movies = [('The Shawshank Redemption', 1994, 'Drama', 1, 8), ('The Green Mile', 1999, 'Drama', 1, 6),
          ('The Godfather', 1972, 'Crime', 2, 7), ('The Godfather III', 1990, 'Crime', 2, 6),
          ('Pulp Fiction', 1994, 'Crime', 3, 9), ('Inglourious Basterds', 2009, 'War', 3, 8),
          ('The Dark Knight', 2008, 'Action', 4, 9), ('Interstellar', 2014, 'Sci-fi', 4, 8),
          ('The Prestige', 2006, 'Drama', 4, 10), ('Fight Club', 1999, 'Drama', 5, 7),
          ('Zodiac', 2007, 'Crime', 5, 5),
          ('Seven', 1995, 'Drama', 5, 8), ('Alien 3', 1992, 'Horror', 5, 5)]

cursor = db_connection.cursor()
cursor.execute(create_db_query)
cursor.execute(create_tables_query)

for director in directors:
    cursor.execute(insert_directors_query, director)
db_connection.commit()

for movie in movies:
    cursor.execute(insert_movies_query, movie)
db_connection.commit()

if __name__ == '__main__':

    select_movies_since_2002 = """SELECT * FROM movies WHERE year > 2002"""

    with db_connection:

        coursor = db_connection.cursor()
        coursor.execute(select_movies_since_2002)
        data_output = coursor.fetchall()
        print(data_output)
