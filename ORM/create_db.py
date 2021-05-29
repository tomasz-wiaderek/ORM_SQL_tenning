from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


engine = create_engine('sqlite:////home/tomasz/PycharmProjects/ORM_SQL_trenning/ORM/cinematics.db')
Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"

    director_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)

    movies = relationship("Movie", back_populates="director")


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(10), nullable=False)
    director_id = Column(Integer, ForeignKey("directors.director_id"))
    rating = Column(Integer, nullable=False)

    director = relationship("Director", back_populates="movies")


Base.metadata.create_all(engine)
