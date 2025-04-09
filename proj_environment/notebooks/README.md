I filen Frost Datasett henter vi data fra MET på ulike ting som vinhastighet, temperatur, nedbør og luftfuktighet.
Denne dataen visualiserer vi i grafer med ulike formater som passer til typen data vi visualiserer.
Videre bruker vi regresjon til å kjøre en prediktiv analyse av datasettet og komme med en informert gjetning på hvordan været vil se ut de neste 14 dagene.

For å velge værstasjonen vi henter data fra bruker vi en geocoder som finner koordinatene til en by som vi selv velger.
Deretter bruker vi disse koordinatene til å velge værstasjon. Vi velger bare den som er nærmest.
Om værstasjonen mangler noe data som vindhastighet eller nedbør, sjekker den nest nærmeste værstasjon. Dette kan den gjøre opp til 15 ganger. 
Denne dataen legger vi inn i en csv fil som vi senere bruker til å plotte dataen. 

Problemet med framgangsmåten er at man av og til kan få data som ikke kommer fra samme sted, men vi har vurdert at det er nøyaktig nok til at vi bruker denne framgangsmåten.