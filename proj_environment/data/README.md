I data lagrer vi alle dataene vi henter knyttet til temperatur, regn, vindhastighet og luftfuktighet i csv filer.
Dette lar oss lettere bruke dataene i senere beregninger og visualisering.
Når vi kjører koden på nytt med andre parametere som, andre byer eller annen tidshorisont, blir dataene overskrevet og det nye settet med data blir lagret.
På denne måten sparer vi plass og unngår eventuell problemer hvor gammel data kan brukes med uhell.
Dette påvirker ikke datakvaliteten på noen viktige måter ettersom vi kun tar dataene som vi trenger og lagrer dem uten å modifisere dem. 
Vi fjerner unødvendig data some TimeOffset, ettersom vi ikke bruker den, men dette påvirker ikke kvaliteten på dataene vi bruker.