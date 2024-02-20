This module is an extension to the Fleet module and gives the user the option to register and expense business trips. The module is based on Dutch tax rules but can be used for mileage registration in general. In the Netherlands one sometimes needs to register the private miles as well, hence we added the (non mandatory) field ‘Is Private trip?’.
This module connects the fleet module to the expense module. In order to be able to expense registered miles on the expense category the checkbox ‘can de used in Fleet module’ should be set to True. On this record it’s also possible to add an analytic account to the category.
We added new fields to the menu ‘Odometers’:
•	New Many2one field: Contact. 
•	New Field: From. Char
•	New Field: To, Char
•	New field: Integer: Single way trip
•	New Field: Boolean: Is_Roundtrip 
New Field: integer: Total km trip
•	If 'is_roundtrip' is false then show value of 'single way trip' else double the single way tip
•	New field: Total km's, calculated field
•	Boolean: Is_Private_trip?
•	Related field: Expense category
•	Non mandatory field odometer reading start. Integer, no logic, user fills in start number
•	Non mandatory field odometer reading end, no logic user fills in end number.
•	Status field: To Expense, Expensed, and not to expense (for private trips)
Note:
•	Employer should be created and linked to user in order to be able to expense
•	On the registered car the default expense category can be added
•	From the listview lines with status ‘to expense’ can be expensed. For each expense category new expenses will be created
•	The user can only expense his/hers own Odometer lines
•	Expensing lines is optional
Feature requests:
•	Change the type for fields ‘From’ and ‘To’ to fields to be used with Open Street


