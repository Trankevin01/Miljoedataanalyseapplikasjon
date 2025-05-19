# Frost Datasett

I filen **Frost Datasett** henter vi data fra MET på ulike ting som:

- Vindhastighet
- Temperatur
- Nedbør
- Luftfuktighet

Denne dataen visualiserer vi i grafer med ulike formater som passer til typen data vi visualiserer. Videre bruker vi regresjon til å kjøre en prediktiv analyse av datasettet og komme med en informert gjetning på hvordan været vil se ut de neste dagene.

## Valg av værstasjon

For å velge værstasjonen vi henter data fra, bruker vi en geocoder som finner koordinatene til en by som vi selv velger. Deretter bruker vi disse koordinatene til å velge værstasjon:

- Vi velger bare den som er nærmest.
- Om værstasjonen mangler noe data som vindhastighet eller nedbør, sjekker den nest nærmeste værstasjonen for å se om den har dataene vi ønsker. 
- Dette kan den gjøre opptil **15 ganger**.

Denne dataen legger vi inn i en **CSV-fil** som vi senere bruker til å plotte dataen.

## Problemer med framgangsmåten

Problemet med framgangsmåten er at man av og til kan få data som ikke kommer fra samme sted. Vi har vurdert at for de fleste stedene i Norge er værstasjonene plassert nærme nok hverandre, og vi vil derfor få data fra ca. samme område selv om det er ulike stasjoner.

## Programfunksjonalitet

Vi lager et program som lar brukeren:

1. Velge et sted i Norge.
2. Se den historiske værdataen til dette stedet.
3. Få se prediksjoner for fremtidig værdata

Programmet henter informasjon fra den nærmeste værstasjonen til det valgte stedet og visualiserer dataene i grafer. Programmet viser også en beregning for hvordan framtidig vær kommer til å se ut. 

All data er hentet fra MET, som er en offentlig kilde sponset av den norske stat.
---