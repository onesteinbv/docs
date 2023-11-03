SEPA betalingen leverancier
===========================

Betalingen aan uw leveranciers doet u eenvoudig door deze via een SEPA XML bestand aan uw bank aan te leveren. Het SEPA bestand komt uit Curq en bevat alle betalingen die u wilt doen op basis van bijvoorbeeld de vervaldatum. Als de bank het bestand heeft verwerkt dan kunt u vervolgens de banktransactie eenvoudig verwerken in Curq.

1. Aanmaken en verwerken van een inkoopfactuur
----------------------------------------------

    Bij het verwerken van de inkoopfactuur hoort het banknummer van de leverancier bekend te zijn en op de klantkaart te zijn ingevuld (anders kan de SEPA betaling niet worden uitgevoerd). Ook dient u de factuurreferentie in te vullen bij de inkoopfactuur (dit is een verplicht veld bij opmaken van het SEPA bestand.

    .. image:: SEPA-betalingen-leverancier-OCA-Media//image1.png
        :width: 6.3in
        :height: 2.90069in

2. Toevoegen en verwerken van inkoopfactuur aan een SEPA bestand via Uitgaande betalingsopdracht
------------------------------------------------------------------------------------------------
    Na bevestigen van de inkoopfactuur kunt u vervolgens de factuur toevoegen aan een SEPA bestand. U maakt een uitgaande betalingsopdracht via het menu ‘Uitgaande betalingsopdracht’. Gebruikt u dit menu dan wordt de status van de inkoopfacturen die u in de batch zet automatisch bijgewerkt als u alle stappen hebt doorlopen.

    Toevoegen via menu Uitgaande betalingen (via Facturatie -> Leveranciers-Uitgaande betaalopdrachten)

    .. image:: SEPA-betalingen-leverancier-OCA-Media//image2.png
       :width: 6.3in
       :height: 2.90069in

    Maak een nieuwe opdracht aan en kies het soort datumfilter. Kies vervolgens voor een vervaldatum. Door vervolgens te klikken op de tekst ‘Toevoegen alle Mutaties’ zal Curq de boekingen tonen die horen bij het gekozen filter.

    Via ‘Aanmaken Transacties’ worden de boekingen in een betaalopdracht gezet

    De betaalopdracht kent verschillende fases. Bij de derde stap (bestand aangemaakt) zal het XML bestand dat u naar de bank kunt uploaden worden aangemaakt. Het uploaden zelf doet u buiten Curq om (rechtstreeks in de applicatie van uw bank).

    As u het bestand heeft ingelezen dan klikt u op de laatste fase, ‘bestand geüpload’. Deze laatste actie zorgt ervoor dat de inkoopfacturen van het bestand in Curq de status ‘Betaald’ krijgen, tevens wordt het totaalbedrag van de te betalen batch op een tussenrekening gezet. (crediteuren onderweg)

    .. image:: SEPA-betalingen-leverancier-OCA-Media//image3.png
       :width: 6.3in
       :height: 2.90069in

3. Boeken in bank
-----------------
    Wanneer het bestand is verwerkt door de bank, de leveranciers zijn betaald, dan krijgt u dit vervolgens te zien in een afschriftregel in uw bank. Deze afschriften kunnen overigens automatisch gesynchroniseerd worden met Curq, gebruik hiervoor de Ponto koppeling die standaard beschikbaar is in Curq (kosten bedragen wel 4 euro per maand per bankrekening, zie voor installatie en gebruik de MyPonto handleiding).

    U lettert de transactieregel af door de eerder gemaakte boeking van de batch te kiezen. De tussenrekening crediteurenrekening wordt hiermee verlaagd met het bedrag en uw bankrekeningsaldo wordt bijgewerkt.

    .. image:: SEPA-betalingen-leverancier-OCA-Media//image4.png
       :width: 6.3in
       :height: 2.90069in
