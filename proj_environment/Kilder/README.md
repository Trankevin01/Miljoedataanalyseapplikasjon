# Kilder

## Værdata

Vi valgte å bruke **frost.met.no API** for å hente værdata. Dette er en offentlig tilgjengelig API som gir tilgang til værdata fra Meteorologisk institutt i Norge. 

- Vi anser denne kilden som pålitelig, ettersom den er offentlig og støttet av den norske staten.

## Koordinater

For å hente ønskede koordinater har vi valgt å bruke **Geopy**. 

- Denne løsningen ble valgt fordi den kan konvertere en adresse eller by til koordinater, som vi deretter bruker til å velge riktig værstasjon.
- Vi stoler på denne kilden basert på egne tester, hvor vi hver gang har fått de koordinatene vi forventer.