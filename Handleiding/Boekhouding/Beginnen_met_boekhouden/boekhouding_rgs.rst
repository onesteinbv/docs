Wat is RGS
---------------------------------------------------------------------------------------------------

Het Referentie Grootboekschema (RGS) is een omvangrijk uniform (grootboek)rekeningschema met als belangrijkste functie het vereenvoudigen van rapportages vanuit de boekhouding. In de praktijk wordt dit bereikt door enerzijds bestaande (grootboek)rekeningschema’s te koppelen aan het ReferentieGrootboekSchema, en anderzijds door rapportages te genereren op basis van het RGS.

Het voordeel van RGS is dat het direct is gekoppeld aan de bron (het grootboek) en dat rapportages daar ook uit kunnen worden afgeleid.

RGS wordt tevens gebruikt als brug om te koppelen aan de rapportageschema’s van bijvoorbeeld SBR en de Productie jaarstatistiek CBS.

RGS in Curq
---------------------------------------------------------------------------------------------------

Wij hebben ervoor gekozen om RGS standaard in te voeren als basis grootboekschema in Curq. Het RGS bevat in totaal 1400 rekeningen per bedrijf, die allemaal zijn ingelezen in Curq. We hebben 600 rekeningen actief gemaakt en 800 op inactief gezet. Als je het aantal actieve grootboeknummers wilt verminderen, kun je dit zelf doen door rekeningen te archiveren (we adviseren om de rekeningen niet te verwijderen maar op inactief te zetten).

Het RGS is volledig geïntegreerd in de boekhouding binnen Curq, inclusief algemene instellingen, BTW-codes, fiscale posities en rapportages zoals BTW ICP-aangifte, Balans en V&W.

Bovenstaande aanpassingen zorgen ervoor dat je direct kunt starten in Curq en in de basis alleen je eigen bankrekeningen hoeft in te voeren om te beginnen met de boekhouding.

Velden van grootboekrekening
---------------------------------------------------------------------------------------------------

.. image:: Media/Rekening.png
   :width: 6.3in
   :height: 2.90069in

**Code**: Dit is een zescijferige code die vanuit het standaard RGS-schema is overgenomen naar Curq. Rapportages zijn niet gebaseerd op dit veld, dus je kunt ervoor kiezen de code aan te passen. Doe dit wel altijd in overleg met je boekhouder.

**Rekeningnaam**: Dit is de omschrijving van het grootboeknummer. Ook dit veld mag je zelf aanpassen; dit heeft geen gevolgen voor de structuur van rapportages.

**Activa profielen**: Hier kun je een standaard activumprofiel invullen als je vanuit een inkoopfactuur direct een activum wilt aanmaken. Curq zal dan bij het invoeren van de grootboekrekening voorstellen om het activum aan te maken en te koppelen aan de inkoopfactuur. De activumprofielen zijn standaard ingericht, maar je kunt hier zelf aanpassingen op doen.

**Soort**: Curq kent verschillende rekeningcategorieën (soort) met een vaste waarde. Elke rekening moet gekoppeld zijn aan een soort, die bijvoorbeeld bepaalt of de rekening onder de balans of onder de verlies- en winstrekening valt. Wijzigen van een categorie heeft invloed op financiële rapportages, dus doe dit alleen in overleg met je boekhouder.

**Standaard BTW**: Als je hier een btw-code invoert, zal Curq deze code altijd voorstellen bij het toevoegen van de rekening op een factuur.

**Labels**: Naast het veld 'soort' om aan te geven onder welke hoofdgroep een rekening valt, is er ook het veld 'labels'. Met een label maak je een verdere detaillering van de hoofdgroep. In Curq is dit veld gerelateerd aan het veld 'groep'. Ons advies is om geen aanpassingen te doen aan het veld 'labels', omdat dit de standaardrapportages beïnvloedt.

**Toegestane dagboeken**: Om ervoor te zorgen dat je bij het kiezen van een grootboekrekening geen onlogische rekeningen selecteert (bijvoorbeeld een kostenrekening bij het invoeren van een verkoopfactuur), hebben we ervoor gezorgd dat het veld 'toegestane dagboeken' is gevuld met logische waarden. Bij elke rekening zie je de dagboek(en) waar de rekening mag worden gebruikt. Als je een rekening selecteert die niet hoort bij het dagboek waarmee je bezig bent, ontvang je een waarschuwing. Je hebt wel de mogelijkheid om ervoor te kiezen het dagboek alsnog aan de rekening toe te voegen.

**Rekening valuta**: Dit dwingt alle boekingsregels in deze rekening om een specifieke valuta te hebben (bijvoorbeeld bankjournalen). Als er geen valuta is ingesteld, kunnen boekingen elke valuta gebruiken.

**Vervallen**: Met dit veld geef je aan of een rekening wel of niet in gebruik is. Je kunt meerdere regels tegelijk selecteren en ze op 'vervallen' zetten.

**Groep**: Dit veld komt vanuit de RGS-standaard, waarbij elke unieke rekening is gekoppeld aan een vaste groep. Je mag en kunt dit veld niet aanpassen. De Balans en V&W-rapportages zijn gebaseerd op dit veld.

**Referentiecode**: De referentiecode binnen het RGS zorgt ervoor dat een rekening uniek wordt geïdentificeerd. De referentiecode is opgebouwd uit vijf niveaus: balans c.q. resultatenrekening (W&V), hoofdrubriek, rubriek, grootboekrekening en mutatie.

RGS kan niet zonder de referentiecode, omdat deze een rekening uniek identificeert en tevens bepaalt met wat voor soort rekening we te maken hebben. De referentiecode begint altijd met de ‘B’ van Balans of de ‘W’ van Winst-en-verliesrekening. Een referentiecode is vervolgens opgebouwd uit groepjes van 3 letters, die de hiërarchische opbouw van RGS aangeven. Een en ander valt eveneens af te leiden uit het onderstaande voorbeeld:

B = Balans (niveau 1) Blim = Liquide middelen (niveau 2) BLimKas = Kasmiddelen (niveau 3) BLimKasKas = Kas (niveau 4 - de feitelijke grootboekrekening)

 (Niveau 5 is niet aanwezig voor de Kas).

**Bedrijf**: Hier wordt het bedrijf getoond dat hoort bij de rekening. Als je werkt met de multi-company optie (alleen beschikbaar vanaf de 'Growth' versie), krijgt ieder bedrijf zijn eigen RGS-inrichting. De administratiegegevens blijven strikt gescheiden.



