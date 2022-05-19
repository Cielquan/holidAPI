# holidAPI

[![maintenance](https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square)](http://unmaintained.tech/)
[![license](https://img.shields.io/github/license/Cielquan/holidapi.svg?style=flat-square&label=License)](https://github.com/Cielquan/holidapi/blob/main/LICENSE)
[![gh_last_commit](https://img.shields.io/github/last-commit/Cielquan/holidapi.svg?style=flat-square&logo=github)](https://github.com/Cielquan/holidapi/commits/main)
[![gh_stars](https://img.shields.io/github/stars/Cielquan/holidapi.svg?style=flat-square&logo=github)](https://github.com/Cielquan/holidapi/stargazers)
[![gh_forks](https://img.shields.io/github/forks/Cielquan/holidapi.svg?style=flat-square&logo=github)](https://github.com/Cielquan/holidapi/network/members)
[![gh_contributors](https://img.shields.io/github/contributors/Cielquan/holidapi.svg?style=flat-square&logo=github)](https://github.com/Cielquan/holidapi/graphs/contributors)
[![gh_watchers](https://img.shields.io/github/watchers/Cielquan/holidapi.svg?style=flat-square&logo=github)](https://github.com/Cielquan/holidapi/watchers/)

**Statische API for deutsch Ferien.**

Dieses Repository stellt eine JSON-API für die deutschen Ferien dar.

## Nutzung

Der `Basislink` ist: `https://cielquan.github.io/holidAPI/api/`.
In den verschiedenen Ordnern sind `holidays.json` Dateien, die die Feriendaten halten.
Jahreszahlen müssen 4-stellig sein.

Bundesländer werden als Zweibuchstabenkürzel angegeben.
Siehe [Wikipedia für Kürzel](https://de.wikipedia.org/wiki/Land_(Deutschland)#Rahmendaten_der_L%C3%A4nder)

- `Basislink`/`holidays.json`: Alle Ferien, die verfügbar sind.
- `Basislink`/`year`/`<JAHR>`/`holidays.json`: Alle Ferien aus dem angegeben Jahr.
- `Basislink`/`year`/`<JAHR>`/`state`/`<BUNDESLAND>`/`holidays.json`: Alle Ferien aus dem angegeben Jahr für das angegebe Bundesland.
- `Basislink`/`state`/`<BUNDESLAND>`/`holidays.json`: Alle Ferien für das angegebe Bundesland.
- `Basislink`/`state`/`<BUNDESLAND>`/`year`/`<JAHR>`/`holidays.json`: Alle Ferien für das angegebe Bundesland aus dem angegeben Jahr.
