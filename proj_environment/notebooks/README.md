I filen Frost Datasett henter vi data fra MET på ulike ting som vinhastighet, temperatur, nedbør og luftfuktighet.
Denne dataen visualiserer vi i grafer med ulike formater som passer til typen data vi visualiserer.
Videre bruker vi regresjon til å kjøre en prediktiv analyse av datasettet og komme med en informert gjetning på hvordan været vil se ut de neste 14 dagene.

For å velge værstasjonen vi henter data fra bruker vi en geocoder som finner koordinatene til en by som vi selv velger.
Deretter bruker vi disse koordinatene til å velge værstasjon. Vi velger bare den som er nærmest.
Om værstasjonen mangler noe data som vindhastighet eller nedbør, sjekker den nest nærmeste værstasjonen for å se om den har dataene vi ønsker. Dette kan den gjøre opp til 15 ganger. 
Denne dataen legger vi inn i en csv fil som vi senere bruker til å plotte dataen. 

Problemet med framgangsmåten er at man av og til kan få data som ikke kommer fra samme sted, men vi har vurdert at de fleste stedene i Norge så er disse værstasjonene plassert nærme nok hverandre og at vi derfor vil få data fra ca. samme område selv om det er ulike stasjoner.

Vi lager et program som lar brukeren velge et sted i Norge og se den historiske værdataene til dette stedet. Programmet henter informasjon fra den nærmeste værstasjonen til det valgte stedet og visualiserer dataene i grafer. Programmet viser også en beregning for hvordan framtidig vær kommer til å se ut. All data er hentet fra MET som er en offentlig kilde sponset fra den norske stat