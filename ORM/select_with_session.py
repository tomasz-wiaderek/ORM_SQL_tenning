from sqlalchemy import and_, between, or_, func, text, distinct
from ORM.create_db import Movie, Director


def select_session_1(session_connection) -> None:
    """Wypisz tytuły filmów z kategorii Crime, które zostały wyprodukowane po roku 1994."""
    result = session_connection.query(Movie.title).filter(and_(Movie.category == 'Crime', Movie.year > 1994)).all()

    print(result)


def select_session_2(session_connection) -> None:
    """Wypisz kategorie wszystkich filmów oraz ich ranking dla filmów, które zostały wyprodukowane w latach 2000-2010 oraz których ranking jest większy niż 7, sortując po rankingu."""
    result = session_connection.query(Movie.category, Movie.title, Movie.rating).filter(and_(
        Movie.rating > 7,
        between(Movie.year, 2000, 2010)
    )).order_by(Movie.rating.desc()).all()

    print(result)


def select_session_3(session_connection) -> None:
    """Wypisz nazwiska wszystkich reżyserów, których ranking jest większy bądź równy 6, a ich imię zaczyna się na literę 'D' lub kończy się na literę 'n'."""
    result = session_connection.query(Director.name, Director.surname, Director.rating).filter(and_(
        Director.rating >= 6,
        or_(Director.name.like("D%"), Director.name.like("%n"))
    )).all()

    print(result)


def select_session_4(session_connection) -> None:
    """Wypisz nazwiska wszystkich reżyserów, których ranking jest większy bądź równy 6, a ich imię zaczyna się na literę 'D' lub kończy się na literę 'n'."""
    result = session_connection.query(Director.name, Director.surname).join(Movie).filter(and_(
        between(Movie.year, 2011, 2014),
        Movie.rating < 9
    )).all()
    print(result)


def select_session_5(session_connection) -> None:
    """Wypisz całkowitą liczbę stworzonych filmów dla każdego reżysera, jego imię i nazwisko, oraz średnią ocen każdego reżysera policzoną na podstawie ocen ich filmów."""
    result = session_connection.query(Director.name, Director.surname, func.count(Director.director_id), func.avg(Movie.rating)).join(Movie).group_by(Director.surname).all()
    print(result)


def select_session_6(session_connection) -> None:
    """Otrzymane z poprzedniego zadania zapytanie, sformatuj do postaci tekstowej używając text(). Zmodyfikuj je tak, aby można było użyć tego zapytania podając przedział lat, w których reżyserowie tworzyli filmy jako parametr do zapytania."""
    raw_sql = text("""
    SELECT directors.name, directors.surname, count(movies.movie_id) AS count_1, avg(movies.rating) AS avg_1 
    FROM directors JOIN movies ON directors.director_id = movies.director_id
    WHERE movies.year BETWEEN :start_year AND :end_year
    GROUP BY directors.director_id
    """)
    result = session_connection.query(
        text("name"), text("surname"), text("count_1"), text("avg_1")
    ).from_statement(raw_sql).params(start_year=1950, end_year=2020).all()
    print(result)


def select_session_7(session_connection, start_year: int, end_year: int) -> None:
    """Do poprzedniego zapytania tekstowego zbinduj parametry korzystając z bind_params(), określając wymagane typy."""
    raw_sql = text("""
    SELECT directors.name, directors.surname, count(movies.movie_id) AS count_1, avg(movies.rating) AS avg_1 
    FROM directors JOIN movies ON directors.director_id = movies.director_id
    WHERE movies.year BETWEEN :start_year AND :end_year
    GROUP BY directors.director_id
    """).bindparams(start_year=start_year, end_year=end_year)

    result = session_connection.query(
        Director.name, Director.surname, text("count_1"), text("avg_1")
    ).from_statement(raw_sql).all()
    print(result)


def select_session_8(session_connection) -> None:
    """Wszystkim reżyserom, których filmy zostały wyprodukowane przed rokiem 2001 oraz ich tytuł zaczyna się na literę 'T', zwiększ oceny o 1."""
    sub_query = session_connection.query(distinct(Movie.director_id)).filter(and_(
        Movie.title.like("T%"),
        Movie.year < 2001
    ))
    session_connection.query(Director).filter(Director.director_id.in_(sub_query)).update({"rating": Director.rating + 1}, synchronize_session=False)
    session_connection.commit()


def select_session_9(session_connection, **kwargs) -> None:
    """Przeprowadź transakcje celem usunięcia z bazy reżysera, używając jego imienia.
    Przetestuj ja dla imienia 'Frank'."""

    if "name" in kwargs:
        condition = Director.name == kwargs["name"]
    elif "surname" in kwargs:
        condition = Director.surname == kwargs["surname"]
    else:
        raise ValueError("Neither name nor surname provided")

    with session_connection.begin():
        subquery = session_connection.query(Director.director_id).filter(condition)
        session_connection.query(Movie).filter(Movie.director_id.in_(subquery)).delete(synchronize_session=False)
        session_connection.query(Director).filter(condition).delete()
