Betalingen
----
In Odoo kunnen betalingen automatisch worden gekoppeld aan een factuur of rekening of het zijn los staande records voor gebruik op een later tijdstip:

Als een betaling is gekoppeld aan een factuur of nota, wordt het verschuldigde bedrag van de factuur verlaagd/verrekend. Je kunt meerdere betalingen aan dezelfde factuur koppelen.

Als een betaling niet aan een factuur of rekening is gekoppeld, heeft de klant een openstaand krediet bij je bedrijf, of heeft je bedrijf een openstaand debet bij een leverancier. Je kunt deze openstaande bedragen gebruiken om onbetaalde facturen/rekeningen te verlagen/vereffenen. Hoe je dit doet vind je terug in het onderdeel 'afletteren'.

Gebruikelijk is om de factuur direct op betaald te zetten als deze binnenkomt op je bankrekening en je deze aflettert, maar Curq ondersteunt ook de mogelijkheid om de (inkoop)factuur handmatig op betaald te zetten. 

Wanneer je inkoopfacturen via SEPA bestanden bij je bank verwerkt, kijk dan bij het onderdeel SEPA inde handleiding hoe je deze betalingen verwerkt (dit gaat in Curq niet via de knop betalingen maar via menu Facturatie-> Leveranciers-> Uitgaande betalingen.

Bankrekening controle
----

Zorg er altijd voor dat je bij aanmaken van een nieuwe leverancier controleert of de gegevens correct zijn. Curq helpt je met controleren van het banknummer. Ook is er een aparte knop waarmee je expliciet aangeeft dat het nummer gecontroleerd is en betalingen gedaan kunnen worden. In onderstaand voorbeeld zie je dat het ingevoerde nummer geen officieel IBAN nummer is. Curq controleert hierop maar omdat er ook niet IBAN nummers toegevoegd kunnen worden, is dit geen blokkerende melding.

Als de schuif 'Betalen' aan staat dan kun je de rekening gebruiken bij betalingen.

.. image:: My-Ponto-Bank-Feed-Media/betalingen_bankrekening.png

Betaling registreren van een factuur of rekening
----

Wanneer je klikt op 'Betaling registreren' in een klantfactuur of factuur van een leverancier, dan wordt een nieuwe journaalpost gegenereerd en wordt het verschuldigde bedrag gewijzigd overeenkomstig het betalingsbedrag. De tegenboeking wordt weergegeven op een rekening voor uitstaande ontvangsten of betalingen. Op dat moment wordt de klantfactuur of leveranciersfactuur gemarkeerd als 'Betaald'. 

Wanneer de openstaande rekening vervolgens wordt afgeletterd met een bankafschriftregel, dan zal Curq automatisch het bedrag op de uitstaande ontvangst of betalingen rekening afboeken en op of afboeken op de bankrekening.

Hieronder zie je de 4 boekingen die Curq maakt bij het op betaald zetten van de factuur en verwerken van de dagafschriftregel.

.. image:: My-Ponto-Bank-Feed-Media/Betalingen_boekingsregel_betaling.png

Het informatiepictogram naast de betalingsregel geeft meer informatie over de betaling weer. Je hebt toegang tot aanvullende informatie, zoals het bijbehorende journaal, door op 'bekijk' te klikken. 

Vanuit dit informatiescherm kun je de aflettering ook ongedaan maken, Dit doe je bijvoorbeeld als je een betaling aan een verkeerde factuur hebt gekoppeld. Na ontkoppelem van de betaling kun je deze eventueel ook verwijderen in het menu Facturatie-> Klanten of leveranciers-> Betalingen

.. image:: My-Ponto-Bank-Feed-Media/betalingen_informatiescherm.png

