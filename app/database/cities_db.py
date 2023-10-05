from attr import define, field
from sqlalchemy import URL, Float, String, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

CITIES_DB_URL: URL = "sqlite:///app/database/cities.db"


class Base(DeclarativeBase):
    pass


class City(Base):
    """ORM schema for city database"""

    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    lat: Mapped[float] = mapped_column(Float())
    lng: Mapped[float] = mapped_column(Float())

    def __repr__(self) -> str:
        return f"City(id={self.id!r}, name={self.name!r}, lat={self.lat!r}, lng={self.lng!r})"


@define(slots=True, auto_attribs=True)
class CitiesDB:
    """Interface for working with city database"""

    _engine: Engine
    _session: Session = field(init=False)

    def __enter__(self) -> "CitiesDB":
        self._session = Session(self._engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self._session.close()

    def get_ids_by_name(self, city_name: str) -> list[int]:
        stmt = select(City).where(City.name == city_name)
        ids = [city.id for city in self._session.scalars(stmt).fetchall()]
        return ids

    def get_coordinates_by_id(self, city_id: int) -> dict[str, float]:
        stmt = select(City).where(City.id == city_id)
        city = self._session.scalars(stmt).fetchall()[0]
        coords = {"lat": city.lat, "lng": city.lng}
        return coords
