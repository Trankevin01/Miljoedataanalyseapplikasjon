# Source

I `src`-mappen har vi lagret API-nøklene, som vi henter via en klasse. 

- Ved å lagre nøklene her unngår vi at de blir direkte tilgjengelige for alle som har tilgang til `Frost Datasett.ipynb`.
- Samtidig kan vi opprettholde en sikker tilkobling.

Denne mappen brukes også til å håndtere funksjonalitet knyttet til **var_data_henting**, som inkluderer:

- Tilkobling til eksterne tjenester for datainnhenting.
- Organisering av kode relatert til datainnhenting og behandling.