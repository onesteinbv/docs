Activa beheer
=============

Het managen van activa in financiële boekhouding is als het zorgvuldig bijhouden en beheren van alles wat een bedrijf in bezit heeft, variërend van fysieke apparatuur tot financiële investeringen en innovatieve concepten. Het begint met het nauwkeurig documenteren van al deze bezittingen en het toekennen van de juiste waarde aan elk item. Om rekening te houden met het feit dat dingen in de loop van de tijd minder waard kunnen worden door bijvoorbeeld slijtage, past activabeheer regelmatig afschrijving toe. Hierdoor wordt de boekwaarde van de activa in de boeken aangepast. Activabeheer houdt ook rekening met potentiële uitdagingen, zoals veroudering van activa en grote economische verschuivingen, en zorgt ervoor dat het bedrijf voldoet aan de geldende regels en voorschriften voor rapportage.

Hier zijn verschillende activa die in de boekhouding worden opgenomen: gebouwen, machines, voertuigen, grond en computerapparatuur. Deze bezittingen vertegenwoordigen de fysieke en technologische middelen van een bedrijf. Ze worden op de balans vermeld om de financiële positie van het bedrijf te weerspiegelen en vormen een belangrijk onderdeel van de totale bedrijfswaarde.

Stel dat jouw bedrijf een machine heeft aangeschaft voor €10.000 met een geschatte levensduur van 5 jaar en een restwaarde van €2.000. De jaarlijkse afschrijving kan worden berekend met de formule:

Afschrijving per jaar= 
(10.000 − 2.000) / 5 = 1600

Dus, de machine zou jaarlijks worden afgeschreven met €1.600. Na het eerste jaar zou de boekwaarde van de machine dan €10.000 - €1.600 = €8.400 zijn, en dit proces zou doorgaan totdat de boekwaarde gelijk is aan de restwaarde na 5 jaar. Afschrijvingen worden vaak toegepast om de kosten van de activa over hun bruikbare levensduur te spreiden in de boekhouding.

Activa Groepen
--------------

Om een duidelijk overzicht te behouden van de activa, is het verstandig om ze te categoriseren in groepen. Deze groepen zullen later de basis vormen voor de indeling in het activarapport. De groepen kan je aanmaken via Facturatie > Configuratie > Activa Groepen.

.. image:: Activa/activa_beheer001.png

- **Naam:** Geef de groep een naam.
- **Code:** Vul een code in.
- **Bovenliggende activagroep:** Koppel een bovenliggende groep als deze groep daaronder valt.

Activa profielen
----------------

Een activaprofiel wordt ingezet om de afschrijvingsmethode van een actief te bepalen. De afschrijvingen worden op basis van dit profiel berekend en financieel verwerkt. Bovendien kan een activaprofiel worden gekoppeld aan een grootboekrekening, zodat bij het boeken van een factuur direct een actief wordt aangemaakt.
Een activaprofiel kan worden aangemaakt via Facturatie > Configuratie > Activa profielen.

.. image:: Activa/activa_beheer002.png

- **Naam:** Geef het activaprofiel een passende naam.
- **Activa Groepen:** Selecteer hier de juiste Activa Groep.
- **Maak een activa aan per product:** Creëer een activa op basis van het product in de boekingsregel, in plaats van alleen op een boekingsregel.
- **Dagboek:** Koppel het dagboek waarin de afschrijvingsboekingen worden aangemaakt.
- **Activa rekening:** Dit is de balansrekening waarop de waarde van de activa wordt bijgehouden.
- **Afschrijvingsrekening:** Hierop worden de waarden van alle afschrijvingen geregistreerd.
- **Waardeverminderingsrekening:** Dit is de kostenrekening waarop de periodieke afschrijvingskosten worden geboekt.
- **Plus-waarde rekening:** Gebruik deze grootboekrekening om pluswaarden te boeken bij verkoop.
- **Min-waarde rekening:** Gebruik deze grootboekrekening om minwaarden te boeken bij verkoop.
- **Resterend rekening bedrag:** Dit is de grootboekrekening voor de restwaarde van het actief.
- **Terugdraaien van journaalposten toestaan:** Maak het mogelijk om boekingen tegen te boeken in plaats van ze te verwijderen.
- **Tijdmethode:** Kies of de afschrijving gebaseerd is op een aantal jaren of een aantal afschrijvingen.
- **Aantal Jaren:** Geef het aantal jaren op.
- **Periodelengte:** Bepaal of de periode per maand, per kwartaal of per jaar is.
- **Gebruik schrikkeljaren:** Bij de berekening van afschrijving wordt rekening gehouden met schrikkeljaren, en dit wordt niet gelijkmatig verdeeld over alle jaren.
- **Berekeningsmethode:** Je kunt een van de volgende methoden kiezen om de afschrijvingsregels te berekenen:
  
  * Lineair: Bereken op basis van de formule: Afschrijvingsbasis / Aantal afschrijvingen. Hierbij is de afschrijvingsbasis gelijk aan de aanschafwaarde minus de restwaarde.
  * Lineair-Limiet: Lineair afschrijven tot aan de restwaarde. De afschrijvingsbasis is gelijk aan de aanschafwaarde.
  * Degressief: Bereken op basis van de formule: Restwaarde * Degressieve Factor.
  * Degressief-Lineair (alleen van toepassing bij Tijdsmethode = Jaar): De degressieve afschrijving wordt lineair wanneer de jaarlijkse lineaire afschrijving groter is dan de jaarlijkse degressieve afschrijving.
  * Degressief-Limiet: Degressief afschrijven tot aan de restwaarde. De afschrijvingsbasis is gelijk aan de waarde van het actief.
  
- **Prorata Temporis:** Bij deze methode wordt de eerste afschrijving berekend op basis van de dag waarop de afschrijving plaatsvindt. Anders wordt een volledige periode gebruikt.
- **Sla concept status over:** Een activum wordt direct geactiveerd als het vanuit een factuur is aangemaakt.

