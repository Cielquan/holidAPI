"""
    models
    ~~~~~~

    Database models and functionality.

    :copyright: (c) 2020, Christian Riedel and AUTHORS
    :license: MIT, see LICENSE
"""  # noqa: D205,D208,D400
# https://www.kmk.org/service/ferien.html
from pathlib import Path

import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship, sessionmaker


states = {
    "BW": "Baden-Württemberg",
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
    "TH": "Thüringen",
}


pub_holidays = {
    "Neujahr": {"wer": "alle", "wann": "01.01."},
    "Heilige Drei Könige": {"wer": ["BW", "BY", "ST"], "wann": "06.01."},
    "Frauentag": {"wer": ["BE"], "wann": "08.03."},
    "Karfreitag": {"wer": "alle", "wann": "OS - 2"},
    "Ostermontag": {"wer": "alle", "wann": "OS + 1"},
    "Tag der Arbeit": {"wer": "alle", "wann": "01.05."},
    "Christi Himmelfahrt": {"wer": "alle", "wann": "OS + 39"},
    "Pfingsmontag": {"wer": "alle", "wann": "OS + 50"},
    "Fronleichnam": {"wer": ["BW", "BY", "HE", "NW", "RP", "SL"], "wann": "OS + 60"},
    "Mariä Himmelfahrt": {"wer": ["SL"], "wann": "15.08."},
    "Weltkindertag": {"wer": ["TH"], "wann": "20.09."},
    "Tag der d. Einheit": {"wer": "alle", "wann": "03.10."},
    "Reformationstag": {"wer": ["BB", "HB", "HH", "MW", "NI", "SN", "ST", "SH", "TH"], "wann": "31.10."},
    "Allerheiligen": {"wer": ["BW", "BY", "NW", "RP", "SL"], "wann": "01.11."},
    "Buß- und Bettag": {"wer": ["SN"], "wann": "Mi vor 23.11."},
    "1. Weihnachtsfeiertag": {"wer": "alle", "wann": "25.12."},
    "2. Weihnachtsfeiertag": {"wer": "alle", "wann": "26.12."},
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
    public_holidays = relationship("PublicHoliday", backref="state")

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

    def __repr__(self) -> str:
        """Represent Holiday model."""
        return (
            f"<holidays(holiday='{self.holiday}', "
            f"state='{self.state}', "
            f"school_year='{self.school_year}', "
            f"start='{self.start}', "
            f"end='{self.end}'>"
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


def fill_holiday_table() -> None:
    pass


def fill_public_holiday_table() -> None:
    pass


def create_db() -> None:
    """Create the database and fill it with defaults."""
    Base.metadata.create_all(engine)
    fill_states_table()
