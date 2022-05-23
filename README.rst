========
holidAPI
========


|maintenance_y| |license|
|gh_last_commit|
|gh_stars| |gh_forks| |gh_contributors| |gh_watchers|


**Statische API for deutsch Ferien.**


Dieses Repository stellt eine JSON-API für die deutschen Ferien dar.
Die Ferien-Daten beginnen mit dem Schuljahr 20/21.


Nutzung
=======

Der ``Basislink`` ist: `<https://cielquan.github.io/holidAPI/api/>`__
In den verschiedenen Ordnern sind ``holidays.json`` Dateien, die die Feriendaten halten.
Jahreszahlen müssen 4-stellig sein.

Bundesländer werden als Zweibuchstabenkürzel angegeben.
Siehe `Wikipedia für Kürzel <https://de.wikipedia.org/wiki/Land_(Deutschland)#Rahmendaten_der_L%C3%A4nder>`__

- ``Basislink``/``holidays.json``: Alle Ferien, die verfügbar sind.
- ``Basislink``/``year``/``<JAHR>``/``holidays.json``: Alle Ferien aus dem angegeben Jahr.
- ``Basislink``/``year``/``<JAHR>``/``state``/``<BUNDESLAND>``/``holidays.json``: Alle Ferien aus dem angegeben Jahr für das angegebe Bundesland.
- ``Basislink``/``state``/``<BUNDESLAND>``/``holidays.json``: Alle Ferien für das angegebe Bundesland.
- ``Basislink``/``state``/``<BUNDESLAND>``/``year``/``<JAHR>``/``holidays.json``: Alle Ferien für das angegebe Bundesland aus dem angegeben Jahr.


.. ############################### LINKS FOR BADGES ###############################


.. General

.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-✖-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - intended

.. |license| image:: https://img.shields.io/github/license/Cielquan/holidapi.svg?style=flat-square&label=License
    :target: https://github.com/Cielquan/holidapi/blob/main/LICENSE
    :alt: License

.. GitHub

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/Cielquan/holidapi.svg?style=flat-square&logo=github
    :target: https://github.com/Cielquan/holidapi/commits/main
    :alt: GitHub - Last Commit

.. |gh_stars| image:: https://img.shields.io/github/stars/Cielquan/holidapi.svg?style=flat-square&logo=github
    :target: https://github.com/Cielquan/holidapi/stargazers
    :alt: Github - Stars

.. |gh_forks| image:: https://img.shields.io/github/forks/Cielquan/holidapi.svg?style=flat-square&logo=github
    :target: https://github.com/Cielquan/holidapi/network/members
    :alt: Github - Forks

.. |gh_contributors| image:: https://img.shields.io/github/contributors/Cielquan/holidapi.svg?style=flat-square&logo=github
    :target: https://github.com/Cielquan/holidapi/graphs/contributors
    :alt: Github - Contributors

.. |gh_watchers| image:: https://img.shields.io/github/watchers/Cielquan/holidapi.svg?style=flat-square&logo=github
    :target: https://github.com/Cielquan/holidapi/watchers/
    :alt: Github - Watchers
