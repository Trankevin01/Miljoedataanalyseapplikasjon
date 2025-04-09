Vi valgte å bruke frost.met.no API for å hente værdata
Dette er en offentlig API som gir tilgang til værdata fra Meteorologisk institutt i Norge.
Vi stoler på denne kilden ettersom det er en offentlig norsk kilde som støttes av den norske stat.

For å hente koordinatene vi ønsker så har vi valgt å bruke geopy.
Dette kommer av at den kan konvertere en adresse/by til koordinater som vi kan bruke for å velge værstasjon.
Vi stoler på denne kilden fordi vi har testet den og funnet ut at den gir de koordinatene vi ønsker hver gang vi prøver.