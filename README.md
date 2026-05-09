# Ohjelmistotekniikka, harjoitustyö Movie Watchlist

Sovelluksessa käyttäjä voi listata elokuvia, joita haluaa tai aikoo katsoa. Katsottuaan elokuvan käyttäjä voi arvioida elokuvan asteikolla 1-5 tähteä.

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](.dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)


## Asennus

1. Asenna riippuvuudet:
 ```bash
poetry install
```

2. Suorita sovelluksen käyttöön alustustoimenpiteet:
 ```bash
poetry run invoke build
```

3. Käynnistä sovellus:
 ```bash
poetry run invoke start
```

## Toiminnot komentoriviltä
### Ohjelman suoritus
Ohjelman voi suorittaa komennolla
```bash
poetry run invoke start
```
### Testaus
Testit saa komennnolla:
```bash
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin saa komennolla:
 ```bash
poetry run invoke coverage-report
```
### Pylint
Tiedostossa [.pylintrc](https://github.com/onnanna/ot-harjoitustyo/blob/main/.pylintrc) määritellyt tarkastukset saa komennolla:
 ```bash
poetry run invoke lint
```
