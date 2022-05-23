"""Create api directory apiure."""
import json

from pathlib import Path
from typing import Generator, List

from models import Holiday, Session, State, db


BASE_DIR = Path() / "docs" / "api"


# UTILS


def query_to_json(query: List) -> str:
    """Take query and turn result into json.

    :param query: query result
    :return: json string of given query
    """
    all_data = [h.to_dict(json_friendly=True) for h in query]
    return json.dumps(all_data, indent=4, sort_keys=True)


def query_to_file(directory: Path, query: List) -> None:
    """Take query and write result as json to file in given directory.

    :param directory: dirtectory to write the file to
    :param query: query to write to the file
    """
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / "holidays.json", "w") as json_file:
        json_file.write(query_to_json(query))


def get_years_from_db() -> Generator:
    """Get all years from the database.

    :return: iterable with all availabe years
    """
    session: db.orm.session.Session = Session()
    return (e[0] for e in set(session.query(Holiday.year).all()))


def get_school_years_from_db() -> Generator:
    """Get all school years from the database.

    :return: iterable with all availabe school years
    """
    session: db.orm.session.Session = Session()
    return (e[0] for e in set(session.query(Holiday.school_year).all()))


# STRUCTURE CREATORS


def create_api() -> None:
    """Wrap all api json file creation functions."""
    session: db.orm.session.Session = Session()
    query_to_file(BASE_DIR, session.query(Holiday).all())
    create_year_state_api()
    create_state_year_api()


def create_year_state_api() -> None:
    """Create api structure sorted by year and then state."""
    session: db.orm.session.Session = Session()

    for year in get_years_from_db():
        year_dir = BASE_DIR / "year" / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)
        query_to_file(year_dir, session.query(Holiday).filter_by(year=year).all())

        for state in session.query(State).all():
            state_dir = year_dir / "state" / state.abbr
            state_dir.mkdir(parents=True, exist_ok=True)
            query_to_file(
                state_dir,
                session.query(Holiday).filter_by(year=year, state_id=state.id).all(),
            )


def create_state_year_api() -> None:
    """Create api structure sorted by state and then year."""
    session: db.orm.session.Session = Session()

    for state in session.query(State).all():
        state_dir = BASE_DIR / "state" / state.abbr
        state_dir.mkdir(parents=True, exist_ok=True)
        query_to_file(
            state_dir, session.query(Holiday).filter_by(state_id=state.id).all()
        )

        for year in get_years_from_db():
            year_dir = state_dir / "year" / str(year)
            year_dir.mkdir(parents=True, exist_ok=True)
            query_to_file(
                year_dir,
                session.query(Holiday).filter_by(year=year, state_id=state.id).all(),
            )


if __name__ == "__main__":
    create_api()
