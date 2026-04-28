# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat listata elokuvia, joita he suunnittelevat katsovansa. Katsotun elokuvan voi arvioida antamalla sille haluamansa määrän tähtiä ja samalla elokuva siirtyy katsottujen elokuvien listalle. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla kaikilla ovat omat elokuvalistansa. 

## Käyttäjät
Aluksi sovelluksella on yksi käyttäjärooli, _normaalikäyttäjä_. Myöhemmin sovellukseen voidaan lisätä toinen käyttäjärooli, _pääkäyttäjä_, jolla on suuremmat oikeudet. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumist
- "tehty" Käyttäjä voi luoda käyttäjätunnuksen järjestelmään
    - "tehty" Käyttäjätunnuksen täytyy olla uniikki ja tietyn mittainen
- "tehty" Käyttäjä voi kirjautua järjestelmään
    - "tehty" Kirjautuminen onnistuu, jos syötetään olemassaoleva käyttäjätunnus ja siihen sopiva salasana
    - "tehty" Jos käyttäjää ei ole olemassa, salasana ei ole oikein tai käyttäjätunnus ei ole oikein, järjestelmä ilmoittaa tästä

### Kirjautumisen jälkeen
- "tehty" Käyttäjä näkee luomansa listan elokuvista
- "tehty" Käyttäjä voi lisätä listalle elokuvan
- "tehty" Käyttäjä voi arvioida katsomansa listalla olevan elokuvan, jolloin elokuva siirtyy katsottujen elokuvien listalle
- "tehty" Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää voidaan täydennetää esim. seuraavanlaisilla ominaisuuksilla:

- Useampien elokuvalistojen luonti esim. genreittäin
- Elokuvan tietojen muokkaaminen
- Elokuvien järjestely arvostelujen mukaan
- Listojen muuttaminen julkisiksi (näkyy muille käyttäjille) tai listan pitäminen yksityisenä
- "tehty" Mahdollisuus lisätä elokuvaan tarkempia tietoja elokuvasta, genre ja muistiinpanoja
- Käyttäjätunnuksen poistaminen
- Listojen poistaminen
- Mahdollisuus järjestellä elokuvia esim. katsomispäivän tai -vuoden mukaan
