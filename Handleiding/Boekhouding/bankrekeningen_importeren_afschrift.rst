Importeren bank transacties
----

Door transacties uit je bankafschriften te importeren, kun je bankrekeningtransacties bijhouden en afstemmen met de transacties in je boekhouding.
Bank synchronisatie automatiseert dit proces. Als je dit echter niet wilt gebruiken of als je bank nog niet wordt ondersteund, zijn er andere opties:

* Importeren van door je bank aangeleverde banktransacties
* Banktransacties handmatig registreren.

.. Note::
   Het groeperen van transacties per afschrift is optioneel.

Transacties importeren
----

Curq ondersteunt meerdere bestandsformaten om transacties te importeren:

* SEPA aanbevolen Cash Management formaat (CAMT.053)
* SEPA aanbevolen Cash Management formaat (CAMT.054)

Om een bestand te importeren, gaat u naar het Boekhouddashboard en klikt u in het Bankjournaal op Transactie importeren.

.. image:: My-Ponto-Bank-Feed-Media/banktransacties_importeren.png

After setting the necessary formatting options and mapping the file columns with their related Odoo fields, you can run a Test and Import your bank transactions.

 Zie ook

Gegevens exporteren en importeren

Register bank transactions manually
You can also record your bank transactions manually. To do so, go to Accounting Dashboard, click on the Bank journal, and then on New. Make sure to fill out the Partner and Label fields to ease the reconciliation process.

Afschriften
A bank statement is a document provided by a bank or financial institution that lists the transactions that have occurred in a particular bank account over a specified period of time.

In Odoo Accounting, it is optional to group transactions by their related statement, but depending on your business flow, you may want to record them for control purposes.

 Belangrijk

If you want to compare the ending balances of your bank statements with the ending balances of your financial records, don’t forget to create an opening transaction to record the bank account balance as of the date you begin synchronizing or importing transactions. This is necessary to ensure the accuracy of your accounting.

To access a list of statements, go to your Accounting Dashboard, click on the vertical ellipsis (⋮) button next to the bank or cash journal you want to check, then on Statements

Statement creation from the kanban view
Open the bank reconciliation view by clicking on the name of the bank journal, and identify the transaction corresponding to the last transaction of your bank statement. Click on the STATEMENT button when hovering on the upper separator line.

A "STATEMENT" button is visible when hovering on the line separating two transactions.
Fill out the statement’s details and save. The newly created statement includes the previous transactions following the last statement.

Statement creation from the list view
Open the list of transactions by clicking on the name of the bank journal and switching to the list view. Select all the transactions corresponding to the bank statement, and, in the Statement column, select an existing statement or create a new one by typing its reference, clicking on Create and edit…, filling out the statement’s details, and saving.
Open the list of transactions by clicking on the name of the bank journal and switching to the list view. Select all the transactions corresponding to the bank statement, and, in the Statement column, select an existing statement or create a new one by typing its reference, clicking on Create and edit…, filling out the statement’s details, and saving.
