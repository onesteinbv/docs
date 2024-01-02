Wat is RGS
----

Het Referentie Grootboekschema (RGS) is een omvangrijk uniform (grootboek)rekeningschema dat als belangrijkste functie heeft rapportages vanuit de boekhouding te vereenvoudigen. Dit laatste wordt in de praktijk bereikt door enerzijds bestaande (grootboek)rekeningschema’s te koppelen aan het ReferentieGrootboekSchema. En anderzijds door rapportages te ontlenen aan het RGS.

Het voordeel van RGS is dat het direct gekoppeld is aan de bron (het grootboek) en rapportages daar ook uit ontleend kunnen worden.

Ook wordt RGS gebruikt als brug om te koppelen aan de rapportageschema’s van bijvoorbeeld SBR en de Productie jaarstatistiek CBS.

RGS in Curq
----

Wij hebben ervoor gekozen om het RGS standaard in te voeren als basis grootboekschema. In totaal bevat het RGS 1400 rekeningen, deze zijn allemaal ingelezen in Curq waarbij we 600 rekeningen op actief hebben gezet en 800 op inactief. Mocht je het aantal actieve grootboeknummers willen verminderen, dan kun je dat altijd zelf doen door rekeningen te archiveren (wij adviseren altijd om de rekeningen niet te verwijderen maar om deze op inactief te zetten). 

**Code**
Dit is een 6 cijferige code die vanuit het standraad RGS schema is overgenomen naar Curq. Rapportages zijn niet op dit veld gebsaeerd dus u kan ervoor kiezen om de code aan te passen.Doe dit wel altijd in overleg met je boekhouder.

**Rekeningnaam**
Dit is de omschrijving van het grootboeknummer. Ook dit veld mag je aanpassen.

**Vervallen**
Met dit veld geef je aan of een rekening wel of niet in gebruik is. Je kunt meerdere regels tegelijk selecteren en die op vervallen zetten.

**Toegestane dagboeken**. Om ervoor te zorgen dat je bij het kiezen van een grootboekrekening geen onlogische rekeningen selecteert (bijvoorbeeld een kostenrekening bij het invoeren van een verkoopfactuur), hebben we besloten om het veld 'toegestane dagboeken' in te vullen met logische waarden. Bij elke rekening zie je de dagboek(en) waar de rekening mag worden gebruikt. Als je een rekening selecteert die niet hoort bij het dagboek waarmee je bezig bent, ontvang je een waarschuwing. Je hebt wel de mogelijkheid om ervoor te kiezen het dagboek alsnog aan de rekening toe te voegen.

**Labels**
Naast het veld soort om aan te geven onder welke hoofgroep een rekening hoort, kennen we ook het veld 'labels'. Met een label wordt een verdere detaillering gemaakt van de groep. In Curq is dit veld gerelateerd aan het veld groep. Ons advies is om geen aanpassingen te doen aan het veld 'labels'omdat dit de standaard rapportages beinvloed. 

**Groep**
Dit veld komt vanuit de RGS standaard, iederee unieke rekening is gekoppeld aan een vaste groep. Je mag en kan dit veld dan ook niet aanpassen. De Balans en V&W rapportages rapportages zijn gebaseerd op dit veld.

**Referentiecode**
De referentiecode binnen het RGS zorgt ervoor dat een rekening uniek geïdentificeerd wordt. De referentiecode is opgebouwd uit vijf niveaus: balans c.q. resultatenrekening (W&V), hoofdrubriek, rubriek, grootboekrekening en mutatie.

RGS kan niet zonder de referentiecode, omdat de referentiecode een rekening uniek identificeert én omdat de referentiecode tevens bepaalt met wat voor soort rekening we hebben te maken. De referentiecode begint altijd begint met de ‘B’ van Balans of de ‘W’ van Winst-en-verliesrekening. Een referentiecode is vervolgens opgebouwd uit groepjes van 3 letters. De groepjes presenteren de hiërarchische opbouw van RGS en geven daar gelijktijdig betekenis aan. Een en ander valt eveneens af te leiden uit onderstaand voorbeeld.

B  = Balans (niveau 1)
Blim = Liquide middelen (niveau 2)
BLimKas = Kasmiddelen (niveau 3)
BLimKasKas = Kas (niveau 4 - de feitelijke grootboekrekening)
(Niveau 5 is niet aanwezig voor de Kas).

**Rekeningcategorie**. Curq kent een aantal categorieen (soort) met een vaste waarde. Iedere rekening moet gekoppeld zijn aan een soort. Wijzigen van een categorie heeft invloed op financiele rapportages, doe dit dus alleen in overleg met je boekhouder. 



