# Enhetstester for Miljødataanalyseapplikasjon

Denne mappen inneholder ulike enhetstester for prosjektet. Testene dekker blant annet:

- **API-nøkkeltester:** Sjekker at API-nøklene fungerer som forventet, både for gyldige og ugyldige nøkler.
- **Datainnhenting:** Tester at data hentes korrekt fra API-et og at feil håndteres riktig.
- **Dataprosessering:** Verifiserer at innhentede data prosesseres og struktureres riktig i DataFrames.
- **Import-tester:** Sikrer at nødvendige moduler og funksjoner kan importeres uten feil.

## Filoversikt

- `enhetstest for api_key. test.py` – Tester for API-nøkkelens funksjonalitet.
- `Negativ Enhetstest API_key.py` – Tester for håndtering av ugyldige API-nøkler.
- `Enhetstest for innhenting av data.py` – Tester for innhenting og prosessering av værdata.
- `Import_enhetstest.py` – Tester at nødvendige imports fungerer.
- `API pulling test.ipynb` – Notebook for å teste API-kall i praksis.