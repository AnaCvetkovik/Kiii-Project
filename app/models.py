from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    director: Mapped[str]
    release_year: Mapped[int]
    genre: Mapped[str]
    rating: Mapped[float]

    def __repr__(self) -> str:
        return f"{self.title!r} ({self.release_year})"