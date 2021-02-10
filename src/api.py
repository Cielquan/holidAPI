"""Create api directory apiure."""
import json

from pathlib import Path
from typing import Generator, List

from models import db, Holiday, Session


BASE_DIR = Path("api")


def query_to_json(query: List) -> str:
    all_data = [h.to_dict(json_friendly=True) for h in query]
    return json.dumps(all_data, indent=4)


def query_to_file(directory, query: List) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / "holidays.json", "w") as json_file:
        json_file.write(query_to_json(query))


def get_years_from_db() -> Generator:
    session: db.orm.session.Session = Session()
    return (e[0] for e in set(session.query(Holiday.year).all()))


def get_school_years_from_db() -> Generator:
    session: db.orm.session.Session = Session()
    return (e[0] for e in set(session.query(Holiday.school_year).all()))


def create_api():
    session: db.orm.session.Session = Session()
    query_to_file(BASE_DIR, session.query(Holiday).all())
    create_year_api()


def create_year_api():
    for year in get_years_from_db():
        subdir = BASE_DIR / "year" / str(year)
        subdir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    create_api()
