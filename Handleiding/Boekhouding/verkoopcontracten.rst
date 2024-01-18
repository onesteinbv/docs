Contracten
----
Met de contractenmodule kun je diensten en of producten als abonnement verkopen. Na aanmaken van een cntract zal Curq op basis van de ingegeven startdatum automatisch de periodieke factuur genereren.
Je kunt een contract los invoeren, maar dit kan ook door eesrt een sjabloon aan te maken. Heb je een vaak terugkerend abonnement dan is het aan te raden om met sjablonen te werken.

De werkwijze bestaat uit de volgende stapen:
1. maak een contract aan, eventueel gebaseerd op een contractsjabloon
2. Geef aan hoe vaak en voor welke periode je het abonnement wil laten lopen
3. Voeg minimaal de verplichte velden aan en voeg de dienst(en) en /of producten die je wil gaan factureren
4. Na ingeven van de velden zal Curq de factuur genereren via een automatisch proces. Voor de eerste factuur kun je ervoor kiezen deze meteen aan te maken via menu 'Handmatig factureren verkoopcontracten'

Aanmaken verkoopcontract
----
Contracten zijn voor klanten te vinden in Facturatie -> Klanten -> Klant en Facturatie  en voor leveranciers onder Leveranciers -> Leverancierscontracten.

Algemene gegevens contract
---
Vul bij het maken van een contract de velden in voor het selecteren van de factureringsparameters:
Contractnaam
Klant of leveranciers naam
Betaalmode
een prijslijst (optioneel)
Verantwoordelijke

facturatie instellingen
-----
Herhalend op regelniveau
Factureer iedere
Factuursoort
Datum eesrte factuur
Diensten
---
En voeg de regels toe waarmee gefactureerd moet worden:
het product met een beschrijving, een hoeveelheid en een prijs
de herhalingsparameters: interval (dagen, weken, maanden, maanden laatste dag of jaren), begindatum, datum van de volgende factuur (automatisch berekend, kan worden gewijzigd) en einddatum (optioneel)
auto-price, om automatisch een prijs uit de prijslijst te laten halen
#START# of #END# in het beschrijvingsveld om de begin-/einddatum van de gefactureerde periode weer te geven in de beschrijving van de factuurregel
pre-paid (factuur aan het begin van de periode) of post-paid (factuur aan het begin van de volgende periode)
De "Generate Recurring Invoices from Contracts" cron draait dagelijks om de facturen te genereren. Als je je in debugmodus bevindt, kun je op de knop voor het aanmaken van facturen klikken.
De snelkoppeling Toon terugkerende facturen op contracten toont alle facturen die zijn aangemaakt op basis van het contract.
Het contractrapport kan worden afgedrukt via het menu Afdrukken.
Het contract kan per e-mail worden verzonden met de knop Verzenden per e-mail
Contractsjablonen kunnen worden aangemaakt via het menu Configuratie -> Contracten -> Contractsjablonen. Hiermee kunnen standaard journaal, prijslijst en regels worden gedefinieerd bij het maken van een contract. Om ze te gebruiken, selecteer je gewoon het sjabloon op het contract en de velden worden automatisch ingevuld.
Contracten verschijnen in het portaal voor de volgende gebruikers in elk contract:
