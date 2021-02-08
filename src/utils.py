"""
    utils
    ~~~~~

    Utility functionality.

    :copyright: (c) 2020, Christian Riedel and AUTHORS
    :license: MIT, see LICENSE for details
"""  # noqa: D205,D208,D400


def calc_easter_sunday(year):
    """Calculate the easter sunday for the given year.

    Calculation is based on Heiner Lichtenberg's correction of Gauss' Easter algorithm.
    Source: https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel

    :param year: year to calculate easter sunday for.
    """
    k = year // 100
    m = 15 + (3 * k + 3) // 4 - (8 * k + 13) // 25
    s = 2 - (3 * k + 3) // 4
    a = year % 19
    d = (19 * a + m) % 30
    r = (d + a // 11) // 29
    og = 21 + d - r
    sz = 7 - (year + year // 4 + s) % 7
    oe = 7 - (og - sz) % 7
    os = og + oe

    easter_date = f"{year}-0{4 if os > 31 else 3}-{(os - 31 if os > 31 else os)}"

    return easter_date
