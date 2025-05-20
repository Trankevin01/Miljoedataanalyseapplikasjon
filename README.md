# Miljødataanalyseapplikasjon

Dette prosjektet analyserer og visualiserer miljødata (værdata) fra åpne kilder, med fokus på innhenting, rensing, analyse, visualisering og prediktiv modellering. Prosjektet er strukturert for å gi praktisk erfaring med datavitenskap, programmering og dokumentasjon.

## Innhold og mappestruktur

- [data/](proj_environment/data/)  
  Inneholder innsamlede og rensede datasett i CSV-format, samt [README](proj_environment/data/README.md) om datakvalitet og overskriving.

- [docs/](proj_environment/docs/)  
  All prosjektdokumentasjon, inkludert [oppgavetekster og vurderingskriterier](proj_environment/docs/tasks/), [KI-deklarasjon](proj_environment/docs/KI/), [oppgavesvar](proj_environment/docs/Oppgavesvar/), og [refleksjonsnotat](proj_environment/docs/Refleksjonsnotat/). Se [README](proj_environment/docs/README.md) for oversikt.

- [Kilder/](proj_environment/Kilder/)  
  Dokumentasjon av datakilder og API-er, med vurdering av pålitelighet. Se [README](proj_environment/Kilder/README.md).

- [notebooks/](proj_environment/notebooks/)  
  Jupyter Notebooks for innhenting ([1_innhenting_av_data.ipynb](proj_environment/notebooks/1_innhenting_av_data.ipynb)), rensing ([2_rensing_av_data.ipynb](proj_environment/notebooks/2_rensing_av_data.ipynb)), og visualisering ([3_plotting_av_data.ipynb](proj_environment/notebooks/3_plotting_av_data.ipynb)) av data. Se [README](proj_environment/notebooks/README.md) for detaljer.

- [src/](proj_environment/src/)  
  Kildekode for håndtering av API-nøkler ([api_key_manager_class.py](proj_environment/src/api_key_manager_class.py)), datainnhenting ([var_data_henting_class.py](proj_environment/src/var_data_henting_class.py)), og annen funksjonalitet. Se [README](proj_environment/src/README.md).

- [tests/](proj_environment/tests/)  
  Enhetstester for prosjektets funksjonalitet, inkludert API-tester og databehandling. Se [README](proj_environment/tests/README.md).

## Installasjon og oppsett

1. Klon repoet og installer avhengigheter fra [requirements.txt](requirements.txt):

   ```sh
   pip install -r requirements.txt
   ```
## Bruk

- Kjør notebookene i [notebooks/](proj_environment/notebooks/) for å hente, rense og analysere data.
- Data lagres og oppdateres automatisk i [data/](proj_environment/data/).
- Visualiseringer og prediktive analyser finnes i de respektive notebookene.

## Dokumentasjon

Se [docs/](proj_environment/docs/) for fullstendig dokumentasjon, oppgavetekster og refleksjonsnotat.

## Kilder

Alle datakilder og API-er er dokumentert i [Kilder/README.md](proj_environment/Kilder/README.md).

---