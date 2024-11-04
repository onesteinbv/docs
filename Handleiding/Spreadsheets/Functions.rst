Functions
=========

Spreadsheetfuncties zijn verdeeld in de volgende categorieën

- :ref:`Array <functions/array>`
- :ref:`Database <functions/database>`
- :ref:`Date <functions/date>`
- :ref:`Engineering <functions/engineering>`
- :ref:`Filter <functions/filter>`
- :ref:`Financial <functions/financial>`
- :ref:`Info <functions/info>`
- :ref:`Logical <functions/logical>`
- :ref:`Lookup <functions/lookup>`
- :ref:`Math <functions/math>`
- :ref:`Misc <functions/misc>`
- :ref:`Odoo <functions/odoo>`
- :ref:`Operators <functions/operators>`
- :ref:`Statistical <functions/statistical>`
- :ref:`Text <functions/text>`
- :ref:`Web <functions/web>`

.. _functions/array:

Array
=====

 - ARRAY.CONSTRAIN(input_range, rows, columns)
 - CHOOSECOLS(array, col_num, [col_num2, ...])
 - CHOOSEROWS(array, row_num, [row_num2, ...])
 - EXPAND(array, rows, [columns], [pad_with])
 - FLATTEN(range, [range2, ...])
 - FREQUENCY(data, classes)
 - HSTACK(range1, [range2, ...])
 - MDETERM(square_matrix)
 - MINVERSE(square_matrix)
 - MMULT(matrix1, matrix2)
 - SUMPRODUCT(range1, [range2, ...])
 - SUMX2MY2(array_x, array_y)
 - SUMX2PY2(array_x, array_y)
 - SUMXMY2(array_x, array_y)
 - TOCOL(array, [ignore], [scan_by_column])
 - TOROW(array, [ignore], [scan_by_column])
 - TRANSPOSE(range)
 - VSTACK(range1, [range2, ...])
 - WRAPCOLS(range, wrap_count, [pad_with])
 - WRAPROWS(range, wrap_count, [pad_with])

.. _functions/database:

Database
========

- DAVERAGE(database, field, criteria)
- DCOUNT(database, field, criteria)
- DCOUNTA(database, field, criteria)
- DGET(database, field, criteria)
- DMAX(database, field, criteria)
- DMIN(database, field, criteria)
- DPRODUCT(database, field, criteria)
- DSTDEV(database, field, criteria)
- DSTDEVP(database, field, criteria)
- DSUM(database, field, criteria)
- DVAR(database, field, criteria)
- DVARP(database, field, criteria)

Date
====

- DATE(year, month, day)
- DATEDIF(start_date, end_date, unit)
- DATEVALUE(date_string)
- DAY(date)
- DAYS(end_date, start_date)
- DAYS360(start_date, end_date, [method])
- EDATE(start_date, months)
- EOMONTH(start_date, months)
- HOUR(time)
- ISOWEEKNUM(date)
- MINUTE(time)
- MONTH(date)
- NETWORKDAYS(start_date, end_date, [holidays])
- NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
- NOW()
- SECOND(time)
- TIME(hour, minute, second)
- TIMEVALUE(time_string)
- TODAY()
- WEEKDAY(date, [type])
- WEEKNUM(date, [type])
- WORKDAY(start_date, num_days, [holidays])
- WORKDAY.INTL(start_date, num_days, [weekend], [holidays])
- YEAR(date)
- YEARFRAC(start_date, end_date, [day_count_convention])
- MONTH.START(date)
- MONTH.END(date)
- QUARTER(date)
- QUARTER.START(date)
- QUARTER.END(date)
- YEAR.START(date)
- YEAR.END(date)
    

 
