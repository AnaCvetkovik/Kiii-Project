from sqlalchemy.orm import Session
from . import models
from . import schemas


def create(db: Session, schema: schemas.MovieSchema):
    """
    Create a movie.

    Args:
        db (Session): The database session object.
        schema (MovieSchema): The movie schema.

    Returns:
        Movie | None: The created movie, unless one with the same ID already exists.
    """

    existing_movie = read(db, schema.id)

    if existing_movie is not None:
        return None

    movie = models.Movie(
        id=schema.id,
        title=schema.title,
        director=schema.director,
        release_year=schema.release_year,
        genre=schema.genre,
        rating=schema.rating,
    )
    db.add(movie)
    db.commit()
    db.refresh(movie)

    return movie


def read(db: Session, id: int):
    """
    Read a movie.

    Args:
        db (Session): The database session object.
        id (int): The ID of the movie.

    Returns:
        Movie | None: The movie, if it exists.
    """

    return db.query(models.Movie).filter(models.Movie.id == id).first()


def update(db: Session, schema: schemas.MovieSchema):
    """
    Update a movie.

    Args:
        db (Session): The database session object.
        schema (MovieSchema): The movie schema.

    Returns:
        Movie | None: The movie, if it exists.
    """

    movie = read(db, schema.id)

    if movie is None:
        return None

    movie.title = schema.title
    movie.director = schema.director
    movie.release_year = schema.release_year
    movie.genre = schema.genre
    movie.rating = schema.rating

    db.commit()
    db.refresh(movie)

    return movie


def delete(db: Session, id: int):
    """
    Delete a movie.

    Args:
        db (Session): The database session object.
        id (int): The ID of the movie.

    Returns:
        Movie | None: The movie, if it exists.
    """

    movie = read(db, id)

    if movie is None:
        return None

    db.delete(movie)
    db.commit()

    return movie


def list_all(db: Session):
    """
    Get all movies.

    Args:
        db (Session): The database session object.

    Returns:
        list[Movie]: The list of all movies.
    """

    return db.query(models.Movie).all()