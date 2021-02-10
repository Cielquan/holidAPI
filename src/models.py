"""
    models
    ~~~~~~

    Database models and functionality.

    :copyright: (c) 2020, Christian Riedel and AUTHORS
    :license: MIT, see LICENSE
"""  # noqa: D205,D208,D400
# https://www.kmk.org/service/ferien.html
import csv

from datetime import date
from pathlib import Path

import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship, sessionmaker


states = {
    "BW": "Baden-Wuerttemberg",
    "BY": "Bayern",
    "BE": "Berlin",
    "BB": "Brandenburg",
    "HB": "Bremen",
    "HH": "Hamburg",
    "HE": "Hessen",
    "MV": "Mecklenburg-Vorpommern",
    "NI": "Niedersachsen",
    "NW": "Nordrhein-Westfalen",
    "RP": "Rheinland-Pfalz",
    "SL": "Saarland",
    "SN": "Sachsen",
    "ST": "Sachsen-Anhalt",
    "SH": "Schleswig-Holstein",
    "TH": "Thueringen",
}


engine = db.create_engine("sqlite:///" + str(Path("holiday.db")))
Session: db.orm.session.Session = sessionmaker(bind=engine)
Base: DeclarativeMeta = declarative_base()


class State(Base):
    """Database model for german states."""

    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)  # noqa: VNE003
    abbr = db.Column(
        "abbrevation", db.String(2), unique=True, index=True, nullable=False
    )
    long_name = db.Column(db.String(25), index=True, nullable=False)
    holidays = relationship("Holiday", backref="state")
    # public_holidays = relationship("PublicHoliday", backref="state")

    def __repr__(self) -> str:
        """Represent State model."""
        return f"<states(abbrevation='{self.abbr}', long_name='{self.long_name}'>"


class Holiday(Base):
    """Database model for german holidays."""

    __tablename__ = "holidays"

    id = db.Column(db.Integer, primary_key=True)  # noqa: VNE003
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    holiday = db.Column(db.String(50), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    school_year = db.Column(db.String(5), index=True, nullable=False)
    start = db.Column(db.DATE, nullable=False)
    end = db.Column(db.DATE, nullable=False)
    comment = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        """Represent Holiday model."""
        return (
            f"<holidays(holiday='{self.holiday}', "
            f"state='{self.state}', "
            f"school_year='{self.school_year}', "
            f"start='{self.start}', "
            f"end='{self.end}', "
            f"comment='{self.comment}'>"
        )


# class PublicHoliday(Base):
#     """Database model for german public holidays."""

#     __tablename__ = "public_holidays"

#     id = db.Column(db.Integer, primary_key=True)  # noqa: VNE003
#     state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
#     holiday = db.Column(db.String(50), index=True, nullable=False)
#     year = db.Column(db.Integer, index=True, nullable=False)
#     school_year = db.Column(db.String(5), index=True, nullable=False)
#     date = db.Column(db.DATE, nullable=False)

#     def __repr__(self) -> str:
#         """Represent PublicHoliday model."""
#         return (
#             f"<public_holidays(public_holiday='{self.holiday}', "
#             f"state='{self.state}', "
#             f"school_year='{self.school_year}', "
#             f"date='{self.date}'>"
#         )


def fill_states_table() -> None:
    """Fill the states table with the german states."""
    session: db.orm.session.Session = Session()
    for model in (State(abbr=k, long_name=states[k]) for k in states):
        session.add(model)
    session.commit()


def create_holiday_entry(row, session) -> Holiday:
    return Holiday(
        state_id=session.query(State).filter_by(long_name=row[0]).first().id,
        holiday=row[1],
        year=int(row[2]),
        school_year=row[3],
        start=date(
            year=int(row[2]),
            month=int(row[4].split(".")[1]),
            day=int(row[4].split(".")[0]),
        ),
        end=date(
            year=int(row[2]),
            month=int(row[5].split(".")[1]),
            day=int(row[5].split(".")[0]),
        ),
        comment=row[6],
    )


def fill_holiday_table() -> None:
    session: db.orm.session.Session = Session()
    for csv_path in Path("data").glob("*.csv"):
        with open(csv_path, "r") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            for row in csv_data:
                if row[0] == "":
                    continue
                session.add(create_holiday_entry(row, session))
    session.commit()


def create_db() -> None:
    """Create the database and fill it with defaults."""
    Base.metadata.create_all(engine)
    fill_states_table()


def recreate_db() -> None:
    Path("holiday.db").unlink(missing_ok=True)
    create_db()
    fill_holiday_table()


if __name__ == "__main__":
    recreate_db()
