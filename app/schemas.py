from pydantic import BaseModel


class MovieSchema(BaseModel):
    id: int
    title: str
    director: str
    release_year: int
    genre: str
    rating: float