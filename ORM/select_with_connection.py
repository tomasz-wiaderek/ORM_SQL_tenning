from ORM.create_db import engine, Movie, Director
from sqlalchemy import select, and_, or_, between, join, func, text


def select_connection_1():
    """Wypisz tytuły filmów z kategorii Crime, które zostały wyprodukowane po roku 1994."""

    connection = engine.connect()
    with connection:
        select_query = select([Movie.title]).where(Movie.category == 'Crime', Movie.year > 1994)
        result = connection.execute(select_query).fetchall()
        print(result)


def select_connection_2():
    """Wypisz kategorie wszystkich filmów oraz ich ranking dla filmów, które zostały wyprodukowane w latach 2000-2010 oraz których ranking jest większy niż 7, sortując po rankingu."""

    connection = engine.connect()
    with connection:
        select_query = select([Movie.category, Movie.title, Movie.rating]).where(and_(
            Movie.rating > 7,
            between(Movie.year, 2000, 2010)
        )).order_by(Movie.rating.desc())
        result = connection.execute(select_query).fetchall()
        print(result)


def select_connection_3():
    """Wypisz nazwiska wszystkich reżyserów, których ranking jest większy bądź równy 6, a ich imię zaczyna się na literę 'D' lub kończy się na literę 'n'."""

    connection = engine.connect()
    with connection:
        select_query = select([Director.name, Director.surname, Director.rating]).where(and_(
            Director.rating >= 6,
            or_(Director.name.like("D%"), Director.name.like("%n"))
        ))
        result = connection.execute(select_query).fetchall()
        print(result)


def select_connection_4():
    """Wypisz imiona oraz nazwiska wszystkich reżyserów, których filmy zostały utworzone w latach 2011-2014, a ocena ich filmów jest mniejsza niż 9."""

    connection = engine.connect()
    with connection:
        select_query = select(Director.name, Director.surname).select_from(join(Director, Movie)).where(
            and_(between(Movie.year, 2011, 2014), Movie.rating < 9))
        result = connection.execute(select_query).fetchall()
        print(result)


def select_connection_5():
    """Wypisz całkowitą liczbę stworzonych filmów dla każdego reżysera, jego imię i nazwisko, oraz średnią ocen każdego reżysera policzoną na podstawie ocen ich filmów."""

    connection = engine.connect()
    with connection:
        select_query = select(Director.name,
                              Director.surname,
                              func.count(Movie.movie_id),
                              func.avg(Movie.rating)
                              ).select_from(join(Director, Movie)).group_by(Director.director_id)
        result = connection.execute(select_query).fetchall()
        print(result)


def select_connection_6():
    """Otrzymane z poprzedniego zadania zapytanie, sformatuj do postaci tekstowej używając text(). Zmodyfikuj je tak, aby można było użyć tego zapytania podając przedział lat, w których reżyserowie tworzyli filmy jako parametr do zapytania."""

    connection = engine.connect()
    with connection:
        raw_sql = text("""SELECT directors.name, directors.surname, count(movies.movie_id) AS count_1, avg(movies.rating) AS avg_1 
    FROM directors JOIN movies ON directors.director_id = movies.director_id
    WHERE movies.year BETWEEN :start_year AND :end_year
    GROUP BY directors.director_id
    """)
        result = connection.execute(raw_sql, start_year=1950, end_year=2020).fetchall()
        print(result)


def select_connection_7(start_year: int, end_year: int):
    """Do poprzedniego zapytania tekstowego zbinduj parametry korzystając z bind_params(), określając wymagane typy."""

    connection = engine.connect()
    with connection:
        raw_sql = text("""
            SELECT directors.name, directors.surname, count(movies.movie_id) AS count_1, avg(movies.rating) AS avg_1 
            FROM directors JOIN movies ON directors.director_id = movies.director_id
            WHERE movies.year BETWEEN :start_year AND :end_year
            GROUP BY directors.director_id
            """).bindparams(start_year=start_year, end_year=end_year)

        result = connection.execute(raw_sql, start_year, end_year).fetchall()
        print(result)
