BTW en Fiscale Posities
=======================

Het bepalen van de juiste BTW-belastingen kan een uitdaging zijn voor jouw boekhouding. Binnen Curq maken we gebruik van BTW codes en de Fiscale Posities om je hiermee te helpen.

De BTW codes zijn al voorgedefinieerd door Curq. Met de Fiscale Posities bepaalt het systeem automatisch de juiste BTW op basis van slimme regels. Deze slimme vertaling kan gebaseerd worden op verplichting BTW-nummer en het land (geleverd of herkomst). De standaard BTW en Grootboekrekeningen kunnen via de regels van de Fiscale Posities vertaald worden naar een andere BTW of Grootboekrekeningen.

Binnen Curq zijn de standaard Fiscale Posities al ingericht. Afhankelijk van jouw bedrijfsvoering kan je in overleg met Accountant dit verder aanpassen specifiek voor jouw bedrijf.

BTW Codes
---------

De BTW Codes vind je terug onder Facturatie > Configuratie > BTW. Je kan ze hier aanpassen door op de BTW Code te klikken.

.. image:: Accounting-Media/taxes_vat_fiscalpositions001.png

- BTW naam: Hier kan je een naam opgeven voor je BTW code. Deze verschijnt overal binnen Curq, dus geef een herkenbare naam mee.

- BTW berekening: Je krijgt hier een aantal opties.

  * Groep van BTW: Hiermee kan je meerdere btw codes combineren in 1 BTW code.
  * Vast: Een vast bedrag als Belasting.
  * Percentage van prijs: Een percentage als Belasting.
  * Percentage van prijs, inclusief BTW: Een percentage als Belasting die rekening houdt met het totaalbedrag inclusief BTW.

- BTW-soort: Hiermee bepaal je waar deze BTW code kan selecteren binnen Curq.
- BTW-over: Hiermee bepaal tot welke soort producten je deze BTW Code kan toepassen.
- Bedrag: Afhankelijk van de instelling bij BTW berekening geef je hier het percentage of bedrag in.

.. image:: Accounting-Media/taxes_vat_fiscalpositions002.png

In de definitie tabblad leg je de belastingregels vast voor facturen of credits. Het is verplicht om minimaal 1 regel te hebben voor grondslag en voor BTW. Je kan hier bepalen welke percentage van de berekende BTW op de grootboekrekening en BTW vak geboekt wordt. Bij de credits worden de regels en vakken vaak omgedraaid.

.. image:: Accounting-Media/taxes_vat_fiscalpositions003.png

Bij Geavanceerde opties kan je de BTW Code nog verder instellen.

- Label op facturen: Dit is de omschrijving welke op de facturen verschijnen.
- BTW-groep: Dit wordt onderaan in een factuur of order bij het totaal getoond. Het totaal van alle BTW Codes wordt opgeteld in deze groep.
- In de analytische kost inbegrepen?: Moet de berekende BTW ook worden opgenomen in de kostenplaats.
- Land: In welke Land is deze BTW Code geldig.
- inclusief BTW: Word de BTW inclusief berekend.
- Beïnvloed grondslag van daarop volgende BTW's?: Als er meerdere BTW Codes worden toegepast, beïnvloed deze BTW Code de grondslag van de volgende BTW Code. Als er meerdere codes wordt toegepast dan houdt Curq rekening met de volgorde van de BTW codes. De codes met een hogere volgorde worden als eerst toegepast.

In Curq zijn de BTW Codes al voor je ingericht. Het kan zijn dat sommige BTW Codes niet van toepassing zijn. Deactiveer deze door de optie Actief uit te zetten.

Fiscale Posities
----------------

De Fiscale Posities vind je terug onder Facturatie > Configuratie > Fiscale Posities. De BTW regio's zijn reeds ingedeeld in Curq. Bijvoorbeeld, voor zakenrelaties in EU worden andere BTW-tarieven gehanteerd. Curq zorgt op deze manier ervoor dat de correcte BTW op de orders en facturen staat. 

.. image:: Accounting-Media/taxes_vat_fiscalpositions004.png
 
Op tabblad [Vervangingstabel BTW] worden de BTW codes vertaald naar de juiste. Aan de linkerkant vind je de standaard BTW die je op de producten kan definiëren. Zodra deze Fiscale Positie is toegepast op jouw order or factuur, dan wordt eerste de standaard BTW herleidt. Vervolgens wordt de BTW code aan de rechterkant toegepast op jouw order of factuur.

Op tabblad [Vervangingstabel Grootboekrekeningen] worden de grootboekrekeningen vertaald naar de juiste. Daar wordt dezelfde principe toepast.

Automatische toepassing
-----------------------

Voor de automatische toepassing van een Fiscale Positie zijn de instellingen rechtsboven van belang. Deze zullen we hier even toelichten.

.. image:: Accounting-Media/taxes_vat_fiscalpositions005.png

- Automatisch detecteren: Voor het automatisch toepassing aan of uit.
- BTW verplicht: De relatie moet voorzien zijn van een BTW-nummers voor automatische toepassing.
- Landengroep: De relatie bevindt zich in een land binnen de Landengroep.
- Land: De relatie bevindt zich in de opgegeven land.

Als er meerdere Fiscale Posities automatisch worden toegepast dan is de volgorde waar deze in staat van belang. In de lijst van alle Fiscale Posities zie je in welke volgorde ze staan. Het is mogelijk om deze volgorde te wijzigen door ze te slepen.

.. image:: Accounting-Media/taxes_vat_fiscalpositions006.png

Handmatige toepassing
---------------------

In sommige gevallen wil je afwijken van de automatisch voorgestelde Fiscale Positie. Dit kan voorkomen als de relatie waar je zaken mee doet in een aparte BTW-regime valt. Je kan de Fiscale Positie vastleggen bij een relatie of in een order / factuur. We adviseren om zoveel mogelijk dit in te stellen op de relatie. Zodra deze relatie wordt gebruikt bij een order / factuur, dan wordt de Fiscale Positie hiervan afgeleid. Je kan dit instellen bij het contact.

.. image:: Accounting-Media/taxes_vat_fiscalpositions007.png

Wil je toch bij een order of factuur dit toepassen dan kan dit onder tabblad [Overige info].

.. image:: Accounting-Media/taxes_vat_fiscalpositions008.png