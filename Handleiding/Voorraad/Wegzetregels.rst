============
Wegzetregels
============

Wegzetregels zijn essentieel voor het correct opslaan van voorraden binnen een bedrijf. Door gebruik te maken van Wegzetregels kun je producten 'automatisch' verplaatsen van ontvangstlocaties naar de meest geschikte plaatsen in het magazijn zelf.

Om toegang te krijgen tot deze functie, ga je naar *Configuratie → Wegzetregels*.
In dit venster zie je een lijst met wegzetregels die eventueel zijn aangemaakt. 
*Belangrijk: Wegzetregels kunnen worden gedefinieerd per 'product/productcategorie' en/of 'verpakkingssoort' (de instelling 'Verpakkingen' moet ingeschakeld zijn in de Voorraad app.*

Bij het aanmaken kun je de volgende velden vullen:

- Wanneer een product aankomt in
- Product
- Productcategorie
- Verpakkingstype 

.. image:: Product-Configuratie-Media/image85.png

- Opslaan naar sublocatie
- Categorie hebben
- Bedrijf 

.. image:: Product-Configuratie-Media/image86.png

Het systeem verplaatst het product naar de locatie die is aangegeven in *Opslaan naar sublocatie* zodra het de locatie bereikt die is opgegeven in het veld *Wanneer product aankomt in*.
Zie onderstaand voorbeeld:

In een magazijnlocatie, WH/Stock, zijn er de volgende sublocaties:

WH/Stock/Smartphones

WH/Stock/Laptops

Als beide artikelen binnenkomen op WH/Stock, dan worden deze automatisch opgeslagen op de sublocatie.
Je kunt dit dus per product doen, maar ook per productcategorie. 

.. image:: Product-Configuratie-Media/image99.png

Prioriteit van wegzetregels
---------------------------
Curq selecteert een wegzetregel op basis van de volgende prioriteitenlijst (van hoog naar laag) totdat een overeenkomst is gevonden:

1. Verpakkingstype en product
2. Verpakkingstype en productcategorie
3. Verpakkingstype
4. Product
5. Productcategorie

Voorbeeld:
----------

.. image:: Product-Configuratie-Media/image100.png

Opslag Categorieën
------------------
De functie *Opslag Categorieën* biedt de meest efficiënte manier om opslaglocaties te beheren in de voorraadmodule, wat de soepele werking van *Wegzetregels* bevordert. De werking van *Wegzetregels* zal verder worden toegelicht in de volgende sectie.

Om deze functie te activeren, ga je naar het menu **Instellingen** en vink je de optie *Opslag Categorieën* aan onder *Magazijn*.

.. image:: Product-Configuratie-Media/image83.png

Klik op de knop *Nieuw* om een nieuwe opslagcategorie toe te voegen. Geef het nieuwe record een naam in het veld *Opslagcategorie*. Kies vervolgens een van de drie opties:

- Als de locatie leeg is
- Als alle producten hetzelfde zijn
- Gemengde producten toestaan, om aan te geven onder welke omstandigheden je een nieuw product wilt toestaan.

.. image:: Product-Configuratie-Media/image84.png

Onder *Capaciteit per verpakking* kun je attributen zoals het type verpakking en de hoeveelheid definiëren.

Onder *Capaciteit per product* kun je een product, de hoeveelheid en de maatteenheid specificeren.
