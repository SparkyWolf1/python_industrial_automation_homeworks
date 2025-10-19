# Domácí úkoly pro Python v industriální automatizaci
## Homework 1
Zobrazení grafu pomocí modulu plotly. 
### Dash Aplikace
Dash aplikace prozatím využívá integrovaný dataset z plotly.express. Mnou zvolený dataset je trochu víc problémový a csv docela chybové bez úprav.

## Homework 2
Aplikace načte data všech obcí a měst, provede výběr na základě zadaných kritérií.
Z tohoto výběru je následně vytvořen dotaz na https://open-meteo.com/en/docs/geocoding-api pro získání GPS souřadnic.
Zpětně získaná data jsou následně spárována se seznamem výběru měst a je vytvořen dotaz na získání aktuálních dat o počasí z api https://geocoding-api.open-meteo.com/v1/search?.
výsledná data jsou složena pomocí dataclass, zobrazena v dash aplikaci a po zmáčknutí tlačítkal uložit do csv v apolikaci dash uložena do souboru csv.