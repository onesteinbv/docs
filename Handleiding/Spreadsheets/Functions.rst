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
.. list-table::
   :header-rows: 1


   * - Name and arguments   
   * - ARRAY.CONSTRAIN(input_range, rows, columns)    
   * - CHOOSECOLS(array, col_num, [col_num2, ...])     
   * - CHOOSEROWS(array, row_num, [row_num2, ...])  
   * - EXPAND(array, rows, [columns], [pad_with])   
   * - FLATTEN(range, [range2, ...])    
   * - FREQUENCY(data, classes)    
   * - HSTACK(range1, [range2, ...])   
   * - MDETERM(square_matrix)   
   * - MINVERSE(square_matrix)    
   * - MMULT(matrix1, matrix2)   
   * - SUMPRODUCT(range1, [range2, ...])    
   * - SUMX2MY2(array_x, array_y)     
   * - SUMX2PY2(array_x, array_y)    
   * - SUMXMY2(array_x, array_y)  
   * - TOCOL(array, [ignore], [scan_by_column])     
   * - TOROW(array, [ignore], [scan_by_column])    
   * - TRANSPOSE(range)   
   * - VSTACK(range1, [range2, ...])    
   * - WRAPCOLS(range, wrap_count, [pad_with])    
   * - WRAPROWS(range, wrap_count, [pad_with])
   

.. _functions/database:

Database
========

.. list-table::
   :header-rows: 1
  

   * - Name and arguments    
   * - DAVERAGE(database, field, criteria)    
   * - DCOUNT(database, field, criteria)    
   * - DCOUNTA(database, field, criteria)     
   * - DGET(database, field, criteria)    
   * - DMAX(database, field, criteria)     
   * - DMIN(database, field, criteria)    
   * - DPRODUCT(database, field, criteria)  
   * - DSTDEV(database, field, criteria)     
   * - DSTDEVP(database, field, criteria)   
   * - DSUM(database, field, criteria) 
   * - DVAR(database, field, criteria)   
   * - DVARP(database, field, criteria)     


Date
====

.. list-table::
   :header-rows: 1
  

   * - Name and arguments    
   * - DATE(year, month, day)   
   * - DATEDIF(start_date, end_date, unit)    
   * - DATEVALUE(date_string)     
   * - DAY(date)
   * - DAYS(end_date, start_date)    
   * - DAYS360(start_date, end_date, [method])  
   * - EDATE(start_date, months)    
   * - EOMONTH(start_date, months)    
   * - HOUR(time)    
   * - ISOWEEKNUM(date)     
   * - MINUTE(time)    
   * - MONTH(date)     
   * - NETWORKDAYS(start_date, end_date, [holidays])     
   * - NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])    
   * - NOW()     
   * - SECOND(time)     
   * - TIME(hour, minute, second)     
   * - TIMEVALUE(time_string) 
   * - TODAY()   
   * - WEEKDAY(date, [type])    
   * - WEEKNUM(date, [type])   
   * - WORKDAY(start_date, num_days, [holidays])   
   * - WORKDAY.INTL(start_date, num_days, [weekend], [holidays])   
   * - YEAR(date)     
   * - YEARFRAC(start_date, end_date, [day_count_convention])
   * - MONTH.START(date)     
   * - MONTH.END(date)   
   * - QUARTER(date)   
   * - QUARTER.START(date)    
   * - QUARTER.END(date)    
   * - YEAR.START(date)    
   * - YEAR.END(date)
     

.. _functions/engineering:

Engineering
===========

.. list-table::
   :header-rows: 1
  
   * - Name and arguments    
   * - DELTA(number1, [number2])
    

.. _functions/filter:

Filter
======

.. list-table::
   :header-rows: 1

   * - Name and arguments     
   * - FILTER(range, condition1, [condition2, ...])     
   * - UNIQUE(range, [by_column], [exactly_once])
 

.. _functions/financial:

Financial
=========

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - ACCRINTM(issue, maturity, rate, redemption, [day_count_convention])
     - `Excel ACCRINTM article <https://support.microsoft.com/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7>`_
   * - AMORLINC(cost, purchase_date, first_period_end, salvage, period, rate, [day_count_convention])
     - `Excel AMORLINC article <https://support.microsoft.com/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8>`_
   * - COUPDAYS(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPDAYS article <https://support.microsoft.com/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671>`_
   * - COUPDAYBS(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPDAYBS article <https://support.microsoft.com/office/coupdaybs-function-eb9a8dfb-2fb2-4c61-8e5d-690b320cf872>`_
   * - COUPDAYSNC(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPDAYSNC article <https://support.microsoft.com/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547>`_
   * - COUPNCD(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPNCD article <https://support.microsoft.com/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f>`_
   * - COUPNUM(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPNUM article <https://support.microsoft.com/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522>`_
   * - COUPPCD(settlement, maturity, frequency, [day_count_convention])
     - `Excel COUPPCD article <https://support.microsoft.com/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3>`_
   * - CUMIPMT(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])
     - `Excel CUMIPMT article <https://support.microsoft.com/office/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606>`_
   * - CUMPRINC(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])
     - `Excel CUMPRINC article <https://support.microsoft.com/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d>`_
   * - DB(cost, salvage, life, period, [month])
     - `Excel DB article <https://support.microsoft.com/office/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7>`_
   * - DDB(cost, salvage, life, period, [factor])
     - `Excel DDB article <https://support.microsoft.com/office/ddb-function-519a7a37-8772-4c96-85c0-ed2c209717a5>`_
   * - DISC(settlement, maturity, price, redemption, [day_count_convention])
     - `Excel DISC article <https://support.microsoft.com/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53>`_
   * - DOLLARDE(fractional_price, unit)
     - `Excel DOLLARDE article <https://support.microsoft.com/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427>`_
   * - DOLLARFR(decimal_price, unit)
     - `Excel DOLLARFR article <https://support.microsoft.com/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495>`_
   * - DURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])
     - `Excel DURATION article <https://support.microsoft.com/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038>`_
   * - EFFECT(nominal_rate, periods_per_year)
     - `Excel EFFECT article <https://support.microsoft.com/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4>`_
   * - FV(rate, number_of_periods, payment_amount, [present_value], [end_or_beginning])
     - `Excel FV article <https://support.microsoft.com/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3>`_
   * - FVSCHEDULE(principal, rate_schedule)
     - `Excel FVSCHEDULE article <https://support.microsoft.com/office/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d>`_
   * - INTRATE(settlement, maturity, investment, redemption, [day_count_convention])
     - `Excel INTRATE article <https://support.microsoft.com/office/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f>`_
   * - IPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])
     - `Excel IPMT article <https://support.microsoft.com/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f>`_
   * - IRR(cashflow_amounts, [rate_guess])
     - `Excel IRR article <https://support.microsoft.com/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc>`_
   * - ISPMT(rate, period, number_of_periods, present_value)
     - `Excel ISPMT article <https://support.microsoft.com/office/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc>`_
   * - MDURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])
     - `Excel MDURATION article <https://support.microsoft.com/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c>`_
   * - MIRR(cashflow_amounts, financing_rate, reinvestment_return_rate)
     - `Excel MIRR article <https://support.microsoft.com/office/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524>`_
   * - NOMINAL(effective_rate, periods_per_year)
     - `Excel NOMINAL article <https://support.microsoft.com/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b>`_
   * - NPER(rate, payment_amount, present_value, [future_value], [end_or_beginning])
     - `Excel NPER article <https://support.microsoft.com/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815>`_
   * - NPV(discount, cashflow1, [cashflow2, ...])
     - `Excel NPV article <https://support.microsoft.com/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568>`_
   * - PDURATION(rate, present_value, future_value)
     - `Excel PDURATION article <https://support.microsoft.com/office/pduration-function-44f33460-5be5-4c90-b857-22308892adaf>`_
   * - PMT(rate, number_of_periods, present_value, [future_value], [end_or_beginning])
     - `Excel PMT article <https://support.microsoft.com/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441>`_
   * - PPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])
     - `Excel PPMT article <https://support.microsoft.com/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b>`_
   * - PV(rate, number_of_periods, payment_amount, [future_value], [end_or_beginning])
     - `Excel PV article <https://support.microsoft.com/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd>`_
   * - PRICE(settlement, maturity, rate, yield, redemption, frequency, [day_count_convention])
     - `Excel PRICE article <https://support.microsoft.com/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a>`_
   * - PRICEDISC(settlement, maturity, discount, redemption, [day_count_convention])
     - `Excel PRICEDISC article <https://support.microsoft.com/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3>`_
   * - PRICEMAT(settlement, maturity, issue, rate, yield, [day_count_convention])
     - `Excel PRICEMAT article <https://support.microsoft.com/office/pricemat-function-52c3b4da-bc7e-476a-989f-a95f675cae77>`_
   * - RATE(number_of_periods, payment_per_period, present_value, [future_value], [end_or_beginning], [rate_guess])
     - `Excel RATE article <https://support.microsoft.com/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce>`_
   * - RECEIVED(settlement, maturity, investment, discount, [day_count_convention])
     - `Excel RECEIVED article <https://support.microsoft.com/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5>`_
   * - RRI(number_of_periods, present_value, future_value)
     - `Excel RRI article <https://support.microsoft.com/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4>`_
   * - SLN(cost, salvage, life)
     - `Excel SLN article <https://support.microsoft.com/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8>`_
   * - SYD(cost, salvage, life, period)
     - `Excel SYD article <https://support.microsoft.com/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27>`_
   * - TBILLPRICE(settlement, maturity, discount)
     - `Excel TBILLPRICE article <https://support.microsoft.com/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2>`_
   * - TBILLEQ(settlement, maturity, discount)
     - `Excel TBILLEQ article <https://support.microsoft.com/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c>`_
   * - TBILLYIELD(settlement, maturity, price)
     - `Excel TBILLYIELD article <https://support.microsoft.com/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba>`_
   * - VDB(cost, salvage, life, start, end, [factor], [no_switch])
     - `Excel VDB article <https://support.microsoft.com/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73>`_
   * - XIRR(cashflow_amounts, cashflow_dates, [rate_guess])
     - `Excel XIRR article <https://support.microsoft.com/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d>`_
   * - XNPV(discount, cashflow_amounts, cashflow_dates)
     - `Excel XNPV article <https://support.microsoft.com/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7>`_
   * - YIELD(settlement, maturity, rate, price, redemption, frequency, [day_count_convention])
     - `Excel YIELD article <https://support.microsoft.com/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe>`_
   * - YIELDDISC(settlement, maturity, price, redemption, [day_count_convention])
     - `Excel YIELDDISC article <https://support.microsoft.com/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7>`_
   * - YIELDMAT(settlement, maturity, issue, rate, price, [day_count_convention])
     - `Excel YIELDMAT article <https://support.microsoft.com/office/yieldmat-function-ba7d1809-0d33-4bcb-96c7-6c56ec62ef6f>`_

.. _functions/info:

Info
====

- CELL(info_type, reference)
- ISERR(value)
- ISERROR(value)
- ISLOGICAL(value)
- ISNA(value)
- ISNONTEXT(value)
- ISNUMBER(value)
- ISTEXT(value)
- ISBLANK(value)
- NA()
 

.. _functions/logical:

Logical
=======

.. list-table::
   :header-rows: 1


   * - Name and arguments   
   * - AND(logical_expression1, [logical_expression2, ...])    
   * - FALSE()    
   * - IF(logical_expression, value_if_true, [value_if_false])     
   * - IFERROR(value, [value_if_error])    
   * - IFNA(value, [value_if_error])    
   * - IFS(condition1, value1, [condition2, ...], [value2, ...])    
   * - NOT(logical_expression)    
   * - OR(logical_expression1, [logical_expression2, ...])    
   * - TRUE()     
   * - XOR(logical_expression1, [logical_expression2, ...])
    

.. _functions/lookup:

Lookup
======

.. list-table::
   :header-rows: 1
   

   * - Name and arguments   
   * - ADDRESS(row, column, [absolute_relative_mode], [use_a1_notation], [sheet])    
   * - COLUMN([cell_reference])   
   * - COLUMNS(range)     
   * - HLOOKUP(search_key, range, index, [is_sorted])     -
   * - INDEX(reference, row, column)    
   * - INDIRECT(reference, [use_a1_notation])   
   * - LOOKUP(search_key, search_array, [result_range])    
   * - MATCH(search_key, range, [search_type])    
   * - PIVOT(pivot_id, measure_name, [domain_field_name, ...], [domain_value, ...])    
   * - PIVOT.HEADER(pivot_id, [domain_field_name, ...], [domain_value, ...])    
   * - PIVOT.TABLE(pivot_id, [row_count], [include_total], [include_column_titles])    
   * - ROW([cell_reference])    
   * - ROWS(range)     
   * - VLOOKUP(search_key, range, index, [is_sorted])    
   * - XLOOKUP(search_key, lookup_range, return_range, [if_not_found], [match_mode], [search_mode])
     

.. _functions/math:

Math
====

.. list-table::
   :header-rows: 1


   * - Name and arguments   
   * - ABS(value)   
   * - ACOS(value)   
   * - ACOSH(value)    
   * - ACOT(value)   
   * - ACOTH(value) 
   * - ASIN(value)    
   * - ASINH(value)     
   * - ATAN(value)     
   * - ATAN2(x, y)    
   * - ATANH(value)   
   * - CEILING(value, [factor])  
   * - CEILING.MATH(number, [significance], [mode])    
   * - CEILING.PRECISE(number, [significance])   
   * - COS(angle) 
   * - COSH(value)     
   * - COT(angle)    
   * - COTH(value)  
   * - COUNTBLANK(value1, [value2, ...])  
   * - COUNTIF(range, criterion)    
   * - COUNTIFS(criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])     
   * - COUNTUNIQUE(value1, [value2, ...])   
   * - COUNTUNIQUEIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])   
   * - CSC(angle)    
   * - CSCH(value) 
   * - DECIMAL(value, base)    
   * - DEGREES(angle)     
   * - EXP(value)    
   * - FLOOR(value, [factor])   
   * - FLOOR.MATH(number, [significance], [mode])    
   * - FLOOR.PRECISE(number, [significance])    
   * - INT(value)    
   * - ISEVEN(value)     
   * - ISO.CEILING(number, [significance])     
   * - ISODD(value)    
   * - LN(value)   
   * - MOD(dividend, divisor)     -
   * - MUNIT(dimension)     
   * - ODD(value)    
   * - PI()    
   * - POWER(base, exponent)    
   * - PRODUCT(factor1, [factor2, ...])     
   * - RAND()    
   * - RANDARRAY([rows], [columns], [min], [max], [whole_number])    
   * - RANDBETWEEN(low, high)    
   * - ROUND(value, [places])    
   * - ROUNDDOWN(value, [places])    
   * - ROUNDUP(value, [places])    
   * - SEC(angle)    
   * - SECH(value)     
   * - SIN(angle)    
   * - SINH(value)   
   * - SQRT(value)    
   * - SUM(value1, [value2, ...])   
   * - SUMIF(criteria_range, criterion, [sum_range])    
   * - SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])    
   * - TAN(angle)     
   * - TANH(value)   
   * - TRUNC(value, [places])
   
.. _functions/misc:

Misc
====

.. list-table::
   :header-rows: 1


   * - Name and arguments
   * - FORMAT.LARGE.NUMBER(value, [unit])
   
.. _functions/odoo:

Odoo
====

.. list-table::
   :header-rows: 1
  

   * - Name and arguments
    
   * - ODOO.CREDIT(account_codes, date_range, [offset], [company_id], [include_unposted])    
   * - ODOO.DEBIT(account_codes, date_range, [offset], [company_id], [include_unposted])  
   * - ODOO.BALANCE(account_codes, date_range, [offset], [company_id], [include_unposted])    
   * - ODOO.FISCALYEAR.START(day, [company_id])  
   * - ODOO.FISCALYEAR.END(day, [company_id])    
   * - ODOO.ACCOUNT.GROUP(type)    
   * - ODOO.CURRENCY.RATE(currency_from, currency_to, [date])     
   * - ODOO.LIST(list_id, index, field_name)    
   * - ODOO.LIST.HEADER(list_id, field_name)     
   * - ODOO.FILTER.VALUE(filter_name)
     

.. _functions/operators:

Operators
=========

.. list-table::
   :header-rows: 1


   * - Name and arguments
   * - ADD(value1, value2)    
   * - CONCAT(value1, value2)    
   * - DIVIDE(dividend, divisor)    
   * - EQ(value1, value2)  
   * - GT(value1, value2)   
   * - GTE(value1, value2)     
   * - LT(value1, value2)    
   * - LTE(value1, value2)   
   * - MINUS(value1, value2)    
   * - MULTIPLY(factor1, factor2)   
   * - NE(value1, value2)     
   * - POW(base, exponent)    
   * - UMINUS(value)     
   * - UNARY.PERCENT(percentage)    
   * - UPLUS(value)
     

.. _functions/statistical:

Statistical
===========

.. list-table::
   :header-rows: 1
   

   * - Name and arguments    
   * - AVEDEV(value1, [value2, ...])     
   * - AVERAGE(value1, [value2, ...])    
   * - AVERAGE.WEIGHTED(values, weights, [additional_values, ...], [additional_weights, ...])    
   * - AVERAGEA(value1, [value2, ...])    
   * - AVERAGEIF(criteria_range, criterion, [average_range])     
   * - AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])    
   * - CORREL(data_y, data_x)   
   * - COUNT(value1, [value2, ...])    
   * - COUNTA(value1, [value2, ...])     
   * - COVAR(data_y, data_x)  
   * - COVARIANCE.P(data_y, data_x)    
   * - COVARIANCE.S(data_y, data_x)    
   * - FORECAST(x, data_y, data_x)    
   * - GROWTH(known_data_y, [known_data_x], [new_data_x], [b])    
   * - INTERCEPT(data_y, data_x)   
   * - LARGE(data, n)     
   * - LINEST(data_y, [data_x], [calculate_b], [verbose])    
   * - LOGEST(data_y, [data_x], [calculate_b], [verbose])    
   * - MATTHEWS(data_x, data_y)    
   * - MAX(value1, [value2, ...])  
   * - MAXA(value1, [value2, ...])   
   * - MAXIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])   
   * - MEDIAN(value1, [value2, ...])   
   * - MIN(value1, [value2, ...])   
   * - MINA(value1, [value2, ...])    
   * - MINIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])     
   * - PEARSON(data_y, data_x)     
   * - PERCENTILE(data, percentile)
   * - PERCENTILE.EXC(data, percentile)   
   * - PERCENTILE.INC(data, percentile) 
   * - POLYFIT.COEFFS(data_y, data_x, order, [intercept])     
   * - POLYFIT.FORECAST(x, data_y, data_x, order, [intercept])    
   * - QUARTILE(data, quartile_number)    
   * - QUARTILE.EXC(data, quartile_number)     
   * - QUARTILE.INC(data, quartile_number)    
   * - RANK(value, data, [is_ascending])    
   * - RSQ(data_y, data_x)    
   * - SMALL(data, n)   
   * - SLOPE(data_y, data_x)     
   * - SPEARMAN(data_y, data_x)   
   * - STDEV(value1, [value2, ...])    
   * - STDEV.P(value1, [value2, ...])     
   * - STDEV.S(value1, [value2, ...])    
   * - STDEVA(value1, [value2, ...])     
   * - STDEVP(value1, [value2, ...])  
   * - STDEVPA(value1, [value2, ...])    
   * - STEYX(data_y, data_x)     
   * - TREND(known_data_y, [known_data_x], [new_data_x], [b])     
   * - VAR(value1, [value2, ...])     
   * - VAR.P(value1, [value2, ...])    
   * - VAR.S(value1, [value2, ...])     
   * - VARA(value1, [value2, ...])     
   * - VARP(value1, [value2, ...])    
   * - VARPA(value1, [value2, ...])   

.. _functions/text:

Text
====

.. list-table::
   :header-rows: 1
 
   * - Name and arguments    
   * - CHAR(table_number)  
   * - CLEAN(text)     
   * - CONCATENATE(string1, [string2, ...])   
   * - EXACT(string1, string2)     
   * - FIND(search_for, text_to_search, [starting_at])    
   * - JOIN(delimiter, value_or_array1, [value_or_array2, ...])   
   * - LEFT(text, [number_of_characters])    
   * - LEN(text) 
   * - LOWER(text)    
   * - MID(text, starting_at, extract_length)     
   * - PROPER(text_to_capitalize)    
   * - REPLACE(text, position, length, new_text)     
   * - RIGHT(text, [number_of_characters])    
   * - SEARCH(search_for, text_to_search, [starting_at])    
   * - SPLIT(text, delimiter, [split_by_each], [remove_empty_text])   
   * - SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number])    
   * - TEXT(number, format)    
   * - TEXTJOIN(delimiter, ignore_empty, text1, [text2, ...])    
   * - TRIM(text)    
   * - UPPER(text)
     
.. _functions/web:

Web
===

.. list-table::
   :header-rows: 1


   * - Name and arguments  
   * - HYPERLINK(url, [link_label])
    
 
