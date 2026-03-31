```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Aloitusruutu"1" -- "1" Ruutu
    Vankila "1" -- "1" Ruutu
    Sattuma "1" -- "1" Ruutu
    Yhteismaa "1" -- "1" Ruutu
    Asemat "?" -- "1" Ruutu
    Laitokset "?" -- "1" Ruutu
    Normaalitkadut "1" -- "1" Ruutu

    Aloitusruutu "1" -- "1" Monopolipeli
    Vankila "1" -- "1" Monopolipeli

    Ruutu "1" -- "*" Toiminto

    Sattuma "1" -- "1" Kortit
    Yhteismaa "1" -- "1" Kortit
    Kortit "1" -- "*" Toiminto

    Normaalitkadut "1" -- "4" Talo
    Normaalitkadut "1" -- "1" Hotelli
    Normaalitkadut "*" -- "1" Pelaaja
    Pelaaja "1" -- "*" Rahaa
```