Wat is RGS
----

Het Referentie Grootboekschema (RGS) is een omvangrijk uniform (grootboek)rekeningschema dat als belangrijkste functie heeft rapportages vanuit de boekhouding te vereenvoudigen. Dit laatste wordt in de praktijk bereikt door enerzijds bestaande (grootboek)rekeningschema’s te koppelen aan het ReferentieGrootboekSchema. En anderzijds door rapportages te ontlenen aan het RGS.

Het voordeel van RGS is dat het direct gekoppeld is aan de bron (het grootboek) en rapportages daar ook uit ontleend kunnen worden.

Ook wordt RGS gebruikt als brug om te koppelen aan de rapportageschema’s van bijvoorbeeld SBR en de Productie jaarstatistiek CBS.

RGS in Curq
----

Wij hebben ervoor gekozen om het RGS standaard in te voeren als basis grootboekschema. In totaal bevat het RGS 1400 rekeningen, deze zijn allemaal ingelezen in Curq waarbij we 600 rekeningen op actief hebben gezet en 800 op inactief. Mocht je het aantal actieve grootboeknummers willen verminderen, dan kun je dat altijd zelf doen door rekeningen te archiveren (wij adviseren altijd om de rekeningen niet te verwijderen maar om deze op inactief te zetten). 

Het RGS is overal doorgevoerd in de boekhouding binnen Curq. Denk hierbij naast de algemene instellingen, de BTW codes, de fiscale posities ook aan alle rapportages zoals BTW ICP aangifte en Balans en V&W. 

Bovenstaande aanpassingen zorgen ervoor dat je direct kan starten in Curq en in de basis alleen je eigen bankrekeningen hoeft in te voeren om te starten met de boekhouding. 

Velden van grootboekrekening
----
.. image:: Afletteren/media/handmatig_afletteren.png
   :width: 6.69306in
   :height: 3.08125in

**Code**: Dit is een 6 cijferige code die vanuit het standaard RGS schema is overgenomen naar Curq. Rapportages zijn niet op dit veld gebaseerd dus je kan ervoor kiezen om de code aan te passen. Doe dit wel altijd in overleg met je boekhouder.

**Rekeningnaam**: Dit is de omschrijving van het grootboeknummer. Ook dit veld mag je zelf aanpassen, dit heeft geen gevolgen voor de structuur van rapportages.

**Activa profielen**: Wanneer je vanuit een inkoopfactuur direct een activum aan wil maken, dan kun je dit veld gebruiken om een standaard activa profiel in te vullen. Bij invoeren van de grootboekrekening zal Curq dan direct voorstellen om het activum aan te maken en te koppelen aan de inkoopfactuur. De activa profielen zijn ook standaard ingericht, daar kun je zelf aanpassingen op doen.

**Soort**: Curq kent een aantal rekening categorieen (soort) met een vaste waarde. Iedere rekening moet gekoppeld zijn aan een soort, de soort bepaalt bijvoorbeeld of de rekening onder de balans of onde de verlies&winstrekening valt. Wijzigen van een categorie heeft invloed op financiele rapportages, doe dit dus alleen in overleg met je boekhouder. 

**Standaard BTW**: Indien je hier een btw code ingeeft, dan zal Curq deze code altijd als standaard voorstellen bij toeveoegen van de rekening op een factuur. 

**Labels**: Naast het veld soort om aan te geven onder welke hoofdgroep een rekening hoort, kennen we ook het veld 'labels'. Met een label wordt een verdere detaillering gemaakt van de hoofdgroep. In Curq is dit veld gerelateerd aan het veld groep. Ons advies is om geen aanpassingen te doen aan het veld 'labels' omdat dit de standaard rapportages beinvloed. 

**Toegestane dagboeken**: Om ervoor te zorgen dat je bij het kiezen van een grootboekrekening geen onlogische rekeningen selecteert (bijvoorbeeld een kostenrekening bij het invoeren van een verkoopfactuur), hebben we ervoor gezorgd het veld 'toegestane dagboeken' te vullen met logische waarden. Bij elke rekening zie je de dagboek(en) waar de rekening mag worden gebruikt. Als je een rekening selecteert die niet hoort bij het dagboek waarmee je bezig bent, ontvang je een waarschuwing. Je hebt wel de mogelijkheid om ervoor te kiezen het dagboek alsnog aan de rekening toe te voegen.

**Rekening valuta**: Dwingt alle boekinsgregels in deze rekening om een specifieke valuta te hebben (d.w.z. bankjournalen). Als er geen valuta is ingesteld, kunnen boekingen elke valuta gebruiken.

**Vervallen**: Met dit veld geef je aan of een rekening wel of niet in gebruik is. Je kunt meerdere regels tegelijk selecteren en die op vervallen zetten.

**Groep**: Dit veld komt vanuit de RGS standaard, iedere unieke rekening is gekoppeld aan een vaste groep. Je mag en kan dit veld dan ook niet aanpassen. De Balans en V&W rapportages rapportages zijn gebaseerd op dit veld.

**Referentiecode**: De referentiecode binnen het RGS zorgt ervoor dat een rekening uniek geïdentificeerd wordt. De referentiecode is opgebouwd uit vijf niveaus: balans c.q. resultatenrekening (W&V), hoofdrubriek, rubriek, grootboekrekening en mutatie.

RGS kan niet zonder de referentiecode, omdat de referentiecode een rekening uniek identificeert én omdat de referentiecode tevens bepaalt met wat voor soort rekening we hebben te maken. De referentiecode begint altijd begint met de ‘B’ van Balans of de ‘W’ van Winst-en-verliesrekening. Een referentiecode is vervolgens opgebouwd uit groepjes van 3 letters. De groepjes presenteren de hiërarchische opbouw van RGS en geven daar gelijktijdig betekenis aan. Een en ander valt eveneens af te leiden uit onderstaand voorbeeld.

B  = Balans (niveau 1)
Blim = Liquide middelen (niveau 2)
BLimKas = Kasmiddelen (niveau 3)
BLimKasKas = Kas (niveau 4 - de feitelijke grootboekrekening)
(Niveau 5 is niet aanwezig voor de Kas).

**Bedrijf**: Hier wordt het bedrijf getoond dat hoort bij de rekening. Indien je werkt met de mult- comany optie (alleen beschikbaar vanaf de 'Growth'versie), dan zal ieder bedrijf zijn eiegen RGS krijgen.




