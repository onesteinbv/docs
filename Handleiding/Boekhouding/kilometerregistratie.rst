Kilometerregistratie
----

Deze module is een uitbreiding op de Wagenpark module en geeft de gebruiker de mogelijkheid om zakelijke ritten te registreren en te declareren. De module is gebaseerd op de Nederlandse belastingregels, maar kan ook worden gebruikt voor kilometerregistratie in het algemeen. In Nederland is het soms nodig om ook de privékilometers te registreren, vandaar dat we het (niet verplichte) veld 'Is privérit' hebben toegevoegd. Deze module verbindt de wagenparkmodule met de onkostenmodule.

Voorbereidingen
----
Om met de module te kunnen werken dien je de volgende zaken in te richten:

- Bij menu werknemers maak je een werknemer aan en koppel je je gebruikersaccount aan de werknemer. 

- Om de geregistreerde kilometers te kunnen declareren in de onkostencategorie moet het selectievakje 'Kan gebruikt worden in de wagenpark module' aangevinkt staan. Bij de categorie is het ook mogelijk om specifieke grootboek -of analytische rekening toe te voegen aan de categorie. Bij de categorie kun je ook de kilometervergoeding ingeven en kiezen voor de eenheid km (kilometer) of mi (miles).

- Bij menu Wagenpark dien je een auto aan te maken, merk en kenteken zijn verplichte velden.

- Op de geregistreerde auto kan de standaard onkostencategorie worden toegevoegd, dit vereenvoudigt de invoer.

Werknemer

.. image:: Kilometerregistratie/km_invulscherm_medewerker.png
       :width: 6.3in
       :height: 2.93264in

Declaratiecategorie

.. image:: Kilometerregistratie/km_invulscherm_declaratie.png
       :width: 6.3in
       :height: 2.93264in

Aanmaken voertuig

.. image:: Kilometerregistratie/km_invulscherm_auto.png
       :width: 6.3in
       :height: 2.93264in

Invulscherm kilometerregistratie
----

We hebben nieuwe velden toegevoegd aan het menu 'Kilometerregistratie'.

- Contact. Bij welke klant ben je geweest?

- Van. Wat was je vertrekpunt?

- Naar. Wat was je bestemming?

- Enkele reis. Afstand van de enkele reis

- Is een retourrit? 

- Totale km-rit. Als 'is een retourrit' niet is aangekruist dan zie je de waarde van 'enkele reis' anders verdubbelt de enkele reis waarde

- Totaal km's. Berekend veld van aantal kilometers 

- Onkostencategorie. De waarde wordt overgenomen van de auto, kan overschreven worden mocht je meerdere categorieeen gebruiken

- Niet verplicht veld kilometerstand start

- Niet verplicht veld kilometerstand einde

Invoerscherm kilometer registratie

.. image:: Kilometerregistratie/km_invulscherm_kilometers.png
       :width: 6.3in
       :height: 2.93264in

Kilometers doorbelasten
----

Vanuit de lijstweergave kun je de regels doorbelasten die de status 'Te declareren' hebben. Je selecteert deze regels, en declareert ze vervolgens via de actieknop. Curq zal de regels per onkosten declaratiecategorie doorbelasten naar de declaratiemodule. De status van de kilometer regels verandert vervolgens naar 'Gedeclareerd'.

.. image:: Kilometerregistratie/km_kilometer_declaratie.png
       :width: 6.3in
       :height: 2.93264in








