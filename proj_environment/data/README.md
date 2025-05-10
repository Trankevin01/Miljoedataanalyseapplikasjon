# Data

I denne mappen lagrer vi alle innhentede data knyttet til:

- **Temperatur**
- **Nedbør**
- **Vindhastighet**
- **Luftfuktighet**

Dataene lagres i **CSV-filer**, noe som gjør det enklere å bruke dem i senere beregninger og visualiseringer.

## Overskriving av data

Når vi kjører koden på nytt med andre parametere, som ulike byer eller tidshorisonter:

- De eksisterende dataene blir **overskrevet**.
- Det nye datasettet blir lagret.

Dette sparer plass og unngår at gamle data ved en feil tas i bruk.

## Datakvalitet

Datakvaliteten påvirkes ikke vesentlig fordi:

- Vi kun lagrer nødvendige data uten å modifisere dem.
- Enkelte unødvendige elementer, som `Level`, fjernes, men dette har ingen betydning for kvaliteten på dataene vi faktisk bruker.