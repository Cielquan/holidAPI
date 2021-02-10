"""
    utils
    ~~~~~

    Utility functionality.

    :copyright: (c) 2020, Christian Riedel and AUTHORS
    :license: MIT, see LICENSE for details
"""  # noqa: D205,D208,D400
from datetime import date, timedelta


def calc_easter_sunday(year: int) -> str:
    """Calculate the easter sunday for the given year.

    Calculation is based on Heiner Lichtenberg's correction of Gauss' Easter algorithm.
    Source: https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel

    :param year: year to calculate easter sunday for.
    :return: iso formatted date
    """
    k = year // 100  # noqa: VNE001
    m = 15 + (3 * k + 3) // 4 - (8 * k + 13) // 25  # noqa: VNE001
    s = 2 - (3 * k + 3) // 4  # noqa: VNE001
    a = year % 19  # noqa: VNE001
    d = (19 * a + m) % 30  # noqa: VNE001
    r = (d + a // 11) // 29  # noqa: VNE001
    og = 21 + d - r
    sz = 7 - (year + year // 4 + s) % 7
    oe = 7 - (og - sz) % 7
    os = og + oe

    easter_date = f"{year}-0{4 if os > 31 else 3}-{(os - 31 if os > 31 else os)}"

    return easter_date


OS = date.fromisoformat(calc_easter_sunday(date.today().year))
pub_holidays = {
    "Neujahr": {"wer": "alle", "wann": "01.01."},
    "Heilige Drei Könige": {"wer": ["BW", "BY", "ST"], "wann": "06.01."},
    "Frauentag": {"wer": ["BE"], "wann": "08.03."},
    "Karfreitag": {"wer": "alle", "wann": OS + timedelta(-2)},
    "Ostermontag": {"wer": "alle", "wann": OS + timedelta(1)},
    "Tag der Arbeit": {"wer": "alle", "wann": "01.05."},
    "Christi Himmelfahrt": {"wer": "alle", "wann": OS + timedelta(39)},
    "Pfingsmontag": {"wer": "alle", "wann": OS + timedelta(50)},
    "Fronleichnam": {
        "wer": ["BW", "BY", "HE", "NW", "RP", "SL"],
        "wann": OS + timedelta(60),
    },
    "Mariä Himmelfahrt": {"wer": ["SL"], "wann": "15.08."},
    "Weltkindertag": {"wer": ["TH"], "wann": "20.09."},
    "Tag der d. Einheit": {"wer": "alle", "wann": "03.10."},
    "Reformationstag": {
        "wer": ["BB", "HB", "HH", "MW", "NI", "SN", "ST", "SH", "TH"],
        "wann": "31.10.",
    },
    "Allerheiligen": {"wer": ["BW", "BY", "NW", "RP", "SL"], "wann": "01.11."},
    "Buß- und Bettag": {"wer": ["SN"], "wann": "Mi vor 23.11."},
    "1. Weihnachtsfeiertag": {"wer": "alle", "wann": "25.12."},
    "2. Weihnachtsfeiertag": {"wer": "alle", "wann": "26.12."},
}
