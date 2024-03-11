Kilometerregistratie
----

Deze module is een uitbreiding op de Fleet module en geeft de gebruiker de mogelijkheid om zakelijke ritten te registreren en te declareren. De module is gebaseerd op de Nederlandse belastingregels, maar kan ook worden gebruikt voor kilometerregistratie in het algemeen. In Nederland is het soms nodig om ook de privékilometers te registreren, vandaar dat we het (niet verplichte) veld 'Is privérit' hebben toegevoegd. Deze module verbindt de wagenparkmodule met de onkostenmodule.

Voorbereidingen
----
Om met de module te kunnen werken dien je de volgende zaken in te richten:

- Bij menu wernemers moet worden aangemaakt en gekoppeld aan gebruiker om te kunnen declareren - Op de geregistreerde auto kan de standaard onkostencategorie worden toegevoegd - Vanuit de listview regels met status 'to exp

Om de geregistreerde kilometers te kunnen declareren in de onkostencategorie moet het selectievakje 'can de used in Fleet module' op True staan. Op dit record is het ook mogelijk om een analytische rekening toe te voegen aan de categorie. 

We hebben nieuwe velden toegevoegd aan het menu 'Kilometerregistratie': 

- Contact

- Van

- Naar

- Enkele reis 

- Is een retourrit

- Totale km-rit - Als 'is een retourrit' is niet aangekruist toon dan de waarde van 'enkele reis' anders verdubbel de enkele reis

- Totaal km's, berekend veld  

- Gerelateerd veld: Onkostencategorie 

- Niet verplicht veld kilometerstand start. Integer, geen logica, gebruiker vult startnummer in 

- Niet verplicht veld kilometerstand einde, geen logica, gebruiker vult eindnummer in. 

- Statusveld: To Expense, Expensed, and not to expense (voor privéritten) Opmerking: 






