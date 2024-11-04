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

.. _functions/engineering:

Engineering
===========

- DELTA(number1, [number2])


Filter
======

- FILTER(range, condition1, [condition2, ...])
- UNIQUE(range, [by_column], [exactly_once])
   
.. _functions/financial:

Financial
=========

- ACCRINTM(issue, maturity, rate, redemption, [day_count_convention])
- AMORLINC(cost, purchase_date, first_period_end, salvage, period, rate, [day_count_convention])
- COUPDAYS(settlement, maturity, frequency, [day_count_convention])
- COUPDAYBS(settlement, maturity, frequency, [day_count_convention])
- COUPDAYSNC(settlement, maturity, frequency, [day_count_convention])
    
   * - COUPNCD(settlement, maturity, frequency, [day_count_convention])
    
   * - COUPNUM(settlement, maturity, frequency, [day_count_convention])
     
   * - COUPPCD(settlement, maturity, frequency, [day_count_convention])
    
   * - CUMIPMT(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])
    
   * - CUMPRINC(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])
   
   * - DB(cost, salvage, life, period, [month])
     
   * - DDB(cost, salvage, life, period, [factor])
    
   * - DISC(settlement, maturity, price, redemption, [day_count_convention])
  
   * - DOLLARDE(fractional_price, unit)
    
   * - DOLLARFR(decimal_price, unit)
    
   * - DURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])
    
   * - EFFECT(nominal_rate, periods_per_year)
   
   * - FV(rate, number_of_periods, payment_amount, [present_value], [end_or_beginning])
  
   * - FVSCHEDULE(principal, rate_schedule)
   
   * - INTRATE(settlement, maturity, investment, redemption, [day_count_convention])
    
   * - IPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])
    
   * - IRR(cashflow_amounts, [rate_guess])
   
   * - ISPMT(rate, period, number_of_periods, present_value)
    
   * - MDURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])
    
   * - MIRR(cashflow_amounts, financing_rate, reinvestment_return_rate)
  
   * - NOMINAL(effective_rate, periods_per_year)
   
   * - NPER(rate, payment_amount, present_value, [future_value], [end_or_beginning])
    
   * - NPV(discount, cashflow1, [cashflow2, ...])
   
   * - PDURATION(rate, present_value, future_value)
    
   * - PMT(rate, number_of_periods, present_value, [future_value], [end_or_beginning])
    
   * - PPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])
   
   * - PV(rate, number_of_periods, payment_amount, [future_value], [end_or_beginning])
   
   * - PRICE(settlement, maturity, rate, yield, redemption, frequency, [day_count_convention])
    
   * - PRICEDISC(settlement, maturity, discount, redemption, [day_count_convention])
    
   * - PRICEMAT(settlement, maturity, issue, rate, yield, [day_count_convention])
    
   * - RATE(number_of_periods, payment_per_period, present_value, [future_value], [end_or_beginning], [rate_guess])
    
   * - RECEIVED(settlement, maturity, investment, discount, [day_count_convention])
    
   * - RRI(number_of_periods, present_value, future_value)
     
   * - SLN(cost, salvage, life)
     
   * - SYD(cost, salvage, life, period)
    
   * - TBILLPRICE(settlement, maturity, discount)
     
   * - TBILLEQ(settlement, maturity, discount)
    
   * - TBILLYIELD(settlement, maturity, price)
     
   * - VDB(cost, salvage, life, start, end, [factor], [no_switch])
 
   * - XIRR(cashflow_amounts, cashflow_dates, [rate_guess])
    
   * - XNPV(discount, cashflow_amounts, cashflow_dates)
    
   * - YIELD(settlement, maturity, rate, price, redemption, frequency, [day_count_convention])
   
   * - YIELDDISC(settlement, maturity, price, redemption, [day_count_convention])
     
   * - YIELDMAT(settlement, maturity, issue, rate, price, [day_count_convention])
    
.. _functions/info:

Info
====

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - CELL(info_type, reference)
     - `Excel CELL article <https://support.microsoft.com/office/cell-function-51bd39a5-f338-4dbe-a33f-955d67c2b2cf>`_
   * - ISERR(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISERROR(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISLOGICAL(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISNA(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISNONTEXT(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISNUMBER(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISTEXT(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - ISBLANK(value)
     - `Excel IS article <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>`_
   * - NA()
     - `Excel NA article <https://support.microsoft.com/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c>`_

.. _functions/logical:

Logical
=======

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - AND(logical_expression1, [logical_expression2, ...])
     - `Excel AND article <https://support.microsoft.com/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9>`_
   * - FALSE()
     - `Excel FALSE article <https://support.microsoft.com/office/false-function-2d58dfa5-9c03-4259-bf8f-f0ae14346904>`_
   * - IF(logical_expression, value_if_true, [value_if_false])
     - `Excel IF article <https://support.microsoft.com/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2>`_
   * - IFERROR(value, [value_if_error])
     - `Excel IFERROR article <https://support.microsoft.com/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611>`_
   * - IFNA(value, [value_if_error])
     - `Excel IFNA article <https://support.microsoft.com/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461>`_
   * - IFS(condition1, value1, [condition2, ...], [value2, ...])
     - `Excel IFS article <https://support.microsoft.com/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45>`_
   * - NOT(logical_expression)
     - `Excel NOT article <https://support.microsoft.com/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77>`_
   * - OR(logical_expression1, [logical_expression2, ...])
     - `Excel OR article <https://support.microsoft.com/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0>`_
   * - TRUE()
     - `Excel TRUE article <https://support.microsoft.com/office/true-function-7652c6e3-8987-48d0-97cd-ef223246b3fb>`_
   * - XOR(logical_expression1, [logical_expression2, ...])
     - `Excel XOR article <https://support.microsoft.com/office/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37>`_

.. _functions/lookup:

Lookup
======

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - ADDRESS(row, column, [absolute_relative_mode], [use_a1_notation], [sheet])
     - `Excel ADDRESS article <https://support.microsoft.com/office/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89>`_
   * - COLUMN([cell_reference])
     - `Excel COLUMN article <https://support.microsoft.com/office/column-function-44e8c754-711c-4df3-9da4-47a55042554b>`_
   * - COLUMNS(range)
     - `Excel COLUMNS article <https://support.microsoft.com/office/columns-function-4e8e7b4e-e603-43e8-b177-956088fa48ca>`_
   * - HLOOKUP(search_key, range, index, [is_sorted])
     - `Excel HLOOKUP article <https://support.microsoft.com/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f>`_
   * - INDEX(reference, row, column)
     - `Excel INDEX article <https://support.microsoft.com/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd>`_
   * - INDIRECT(reference, [use_a1_notation])
     - `Excel INDIRECT article <https://support.microsoft.com/office/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261>`_
   * - LOOKUP(search_key, search_array, [result_range])
     - `Excel LOOKUP article <https://support.microsoft.com/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb>`_
   * - MATCH(search_key, range, [search_type])
     - `Excel MATCH article <https://support.microsoft.com/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a>`_
   * - PIVOT(pivot_id, measure_name, [domain_field_name, ...], [domain_value, ...])
     - Get the value from a pivot (not compatible with Excel)
   * - PIVOT.HEADER(pivot_id, [domain_field_name, ...], [domain_value, ...])
     - Get the header of a pivot (not compatible with Excel)
   * - PIVOT.TABLE(pivot_id, [row_count], [include_total], [include_column_titles])
     - Get a pivot table (not compatible with Excel)
   * - ROW([cell_reference])
     - `Excel ROW article <https://support.microsoft.com/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d>`_
   * - ROWS(range)
     - `Excel ROWS article <https://support.microsoft.com/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597>`_
   * - VLOOKUP(search_key, range, index, [is_sorted])
     - `Excel VLOOKUP article <https://support.microsoft.com/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1>`_
   * - XLOOKUP(search_key, lookup_range, return_range, [if_not_found], [match_mode], [search_mode])
     - `Excel XLOOKUP article <https://support.microsoft.com/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929>`_

.. _functions/math:

Math
====

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - ABS(value)
     - `Excel ABS article <https://support.microsoft.com/office/abs-function-3420200f-5628-4e8c-99da-c99d7c87713c>`_
   * - ACOS(value)
     - `Excel ACOS article <https://support.microsoft.com/office/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b>`_
   * - ACOSH(value)
     - `Excel ACOSH article <https://support.microsoft.com/office/acosh-function-e3992cc1-103f-4e72-9f04-624b9ef5ebfe>`_
   * - ACOT(value)
     - `Excel ACOT article <https://support.microsoft.com/office/acot-function-dc7e5008-fe6b-402e-bdd6-2eea8383d905>`_
   * - ACOTH(value)
     - `Excel ACOTH article <https://support.microsoft.com/office/acoth-function-cc49480f-f684-4171-9fc5-73e4e852300f>`_
   * - ASIN(value)
     - `Excel ASIN article <https://support.microsoft.com/office/asin-function-81fb95e5-6d6f-48c4-bc45-58f955c6d347>`_
   * - ASINH(value)
     - `Excel ASINH article <https://support.microsoft.com/office/asinh-function-4e00475a-067a-43cf-926a-765b0249717c>`_
   * - ATAN(value)
     - `Excel ATAN article <https://support.microsoft.com/office/atan-function-50746fa8-630a-406b-81d0-4a2aed395543>`_
   * - ATAN2(x, y)
     - `Excel ATAN2 article <https://support.microsoft.com/office/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033>`_
   * - ATANH(value)
     - `Excel ATANH article <https://support.microsoft.com/office/atanh-function-3cd65768-0de7-4f1d-b312-d01c8c930d90>`_
   * - CEILING(value, [factor])
     - `Excel CEILING article <https://support.microsoft.com/office/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f>`_
   * - CEILING.MATH(number, [significance], [mode])
     - `Excel CEILING.MATH article <https://support.microsoft.com/office/ceiling-math-function-80f95d2f-b499-4eee-9f16-f795a8e306c8>`_
   * - CEILING.PRECISE(number, [significance])
     - `Excel CEILING.PRECISE article <https://support.microsoft.com/office/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb>`_
   * - COS(angle)
     - `Excel COS article <https://support.microsoft.com/office/cos-function-0fb808a5-95d6-4553-8148-22aebdce5f05>`_
   * - COSH(value)
     - `Excel COSH article <https://support.microsoft.com/office/cosh-function-e460d426-c471-43e8-9540-a57ff3b70555>`_
   * - COT(angle)
     - `Excel COT article <https://support.microsoft.com/office/cot-function-c446f34d-6fe4-40dc-84f8-cf59e5f5e31a>`_
   * - COTH(value)
     - `Excel COTH article <https://support.microsoft.com/office/coth-function-2e0b4cb6-0ba0-403e-aed4-deaa71b49df5>`_
   * - COUNTBLANK(value1, [value2, ...])
     - `Excel COUNTBLANK article <https://support.microsoft.com/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22>`_
   * - COUNTIF(range, criterion)
     - `Excel COUNTIF article <https://support.microsoft.com/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34>`_
   * - COUNTIFS(criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - `Excel COUNTIFS article <https://support.microsoft.com/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842>`_
   * - COUNTUNIQUE(value1, [value2, ...])
     - Counts number of unique values in a range (not compatible with Excel)
   * - COUNTUNIQUEIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - Counts number of unique values in a range, filtered by a set of criteria (not compatible with Excel)
   * - CSC(angle)
     - `Excel CSC article <https://support.microsoft.com/office/csc-function-07379361-219a-4398-8675-07ddc4f135c1>`_
   * - CSCH(value)
     - `Excel CSCH article <https://support.microsoft.com/office/csch-function-f58f2c22-eb75-4dd6-84f4-a503527f8eeb>`_
   * - DECIMAL(value, base)
     - `Excel DECIMAL article <https://support.microsoft.com/office/decimal-function-ee554665-6176-46ef-82de-0a283658da2e>`_
   * - DEGREES(angle)
     - `Excel DEGREES article <https://support.microsoft.com/office/degrees-function-4d6ec4db-e694-4b94-ace0-1cc3f61f9ba1>`_
   * - EXP(value)
     - `Excel EXP article <https://support.microsoft.com/office/exp-function-c578f034-2c45-4c37-bc8c-329660a63abe>`_
   * - FLOOR(value, [factor])
     - `Excel FLOOR article <https://support.microsoft.com/office/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886>`_
   * - FLOOR.MATH(number, [significance], [mode])
     - `Excel FLOOR.MATH article <https://support.microsoft.com/office/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5>`_
   * - FLOOR.PRECISE(number, [significance])
     - `Excel FLOOR.PRECISE article <https://support.microsoft.com/office/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e>`_
   * - INT(value)
     - `Excel INT article <https://support.microsoft.com/office/int-function-a6c4af9e-356d-4369-ab6a-cb1fd9d343ef>`_
   * - ISEVEN(value)
     - `Excel ISEVEN article <https://support.microsoft.com/office/iseven-function-aa15929a-d77b-4fbb-92f4-2f479af55356>`_
   * - ISO.CEILING(number, [significance])
     - `Excel ISO.CEILING article <https://support.microsoft.com/office/iso-ceiling-function-e587bb73-6cc2-4113-b664-ff5b09859a83>`_
   * - ISODD(value)
     - `Excel ISODD article <https://support.microsoft.com/office/isodd-function-1208a56d-4f10-4f44-a5fc-648cafd6c07a>`_
   * - LN(value)
     - `Excel LN article <https://support.microsoft.com/office/ln-function-81fe1ed7-dac9-4acd-ba1d-07a142c6118f>`_
   * - MOD(dividend, divisor)
     - `Excel MOD article <https://support.microsoft.com/office/mod-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3>`_
   * - MUNIT(dimension)
     - `Excel MUNIT article <https://support.microsoft.com/office/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3>`_
   * - ODD(value)
     - `Excel ODD article <https://support.microsoft.com/office/odd-function-deae64eb-e08a-4c88-8b40-6d0b42575c98>`_
   * - PI()
     - `Excel PI article <https://support.microsoft.com/office/pi-function-264199d0-a3ba-46b8-975a-c4a04608989b>`_
   * - POWER(base, exponent)
     - `Excel POWER article <https://support.microsoft.com/office/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a>`_
   * - PRODUCT(factor1, [factor2, ...])
     - `Excel PRODUCT article <https://support.microsoft.com/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce>`_
   * - RAND()
     - `Excel RAND article <https://support.microsoft.com/office/rand-function-4cbfa695-8869-4788-8d90-021ea9f5be73>`_
   * - RANDARRAY([rows], [columns], [min], [max], [whole_number])
     - `Excel RANDARRAY article <https://support.microsoft.com/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33>`_
   * - RANDBETWEEN(low, high)
     - `Excel RANDBETWEEN article <https://support.microsoft.com/office/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685>`_
   * - ROUND(value, [places])
     - `Excel ROUND article <https://support.microsoft.com/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c>`_
   * - ROUNDDOWN(value, [places])
     - `Excel ROUNDDOWN article <https://support.microsoft.com/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53>`_
   * - ROUNDUP(value, [places])
     - `Excel ROUNDUP article <https://support.microsoft.com/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7>`_
   * - SEC(angle)
     - `Excel SEC article <https://support.microsoft.com/office/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7>`_
   * - SECH(value)
     - `Excel SECH article <https://support.microsoft.com/office/sech-function-e05a789f-5ff7-4d7f-984a-5edb9b09556f>`_
   * - SIN(angle)
     - `Excel SIN article <https://support.microsoft.com/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602>`_
   * - SINH(value)
     - `Excel SINH article <https://support.microsoft.com/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7>`_
   * - SQRT(value)
     - `Excel SQRT article <https://support.microsoft.com/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf>`_
   * - SUM(value1, [value2, ...])
     - `Excel SUM article <https://support.microsoft.com/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89>`_
   * - SUMIF(criteria_range, criterion, [sum_range])
     - `Excel SUMIF article <https://support.microsoft.com/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b>`_
   * - SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - `Excel SUMIFS article <https://support.microsoft.com/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b>`_
   * - TAN(angle)
     - `Excel TAN article <https://support.microsoft.com/office/tan-function-08851a40-179f-4052-b789-d7f699447401>`_
   * - TANH(value)
     - `Excel TANH article <https://support.microsoft.com/office/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c>`_
   * - TRUNC(value, [places])
     - `Excel TRUNC article <https://support.microsoft.com/office/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721>`_

.. _functions/misc:

Misc
====

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - FORMAT.LARGE.NUMBER(value, [unit])
     - Apply a large number format (not compatible with Excel)

.. _functions/odoo:

Odoo
====

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - ODOO.CREDIT(account_codes, date_range, [offset], [company_id], [include_unposted])
     - Get the total credit for the specified account(s) and period (not compatible with Excel)
   * - ODOO.DEBIT(account_codes, date_range, [offset], [company_id], [include_unposted])
     - Get the total debit for the specified account(s) and period (not compatible with Excel)
   * - ODOO.BALANCE(account_codes, date_range, [offset], [company_id], [include_unposted])
     - Get the total balance for the specified account(s) and period (not compatible with Excel)
   * - ODOO.FISCALYEAR.START(day, [company_id])
     - Returns the starting date of the fiscal year encompassing the provided date (not compatible with Excel)
   * - ODOO.FISCALYEAR.END(day, [company_id])
     - Returns the ending date of the fiscal year encompassing the provided date (not compatible with Excel)
   * - ODOO.ACCOUNT.GROUP(type)
     - Returns the account ids of a given group (not compatible with Excel)
   * - ODOO.CURRENCY.RATE(currency_from, currency_to, [date])
     - This function takes in two currency codes as arguments, and returns the exchange rate from the first currency to the second as float (not compatible with Excel)
   * - ODOO.LIST(list_id, index, field_name)
     - Get the value from a list (not compatible with Excel)
   * - ODOO.LIST.HEADER(list_id, field_name)
     - Get the header of a list (not compatible with Excel)
   * - ODOO.FILTER.VALUE(filter_name)
     - Return the current value of a spreadsheet filter (not compatible with Excel)

.. _functions/operators:

Operators
=========

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - ADD(value1, value2)
     - Sum of two numbers (not compatible with Excel)
   * - CONCAT(value1, value2)
     - `Excel CONCAT article <https://support.microsoft.com/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2>`_
   * - DIVIDE(dividend, divisor)
     - One number divided by another (not compatible with Excel)
   * - EQ(value1, value2)
     - Equal (not compatible with Excel)
   * - GT(value1, value2)
     - Strictly greater than (not compatible with Excel)
   * - GTE(value1, value2)
     - Greater than or equal to (not compatible with Excel)
   * - LT(value1, value2)
     - Less than (not compatible with Excel)
   * - LTE(value1, value2)
     - Less than or equal to (not compatible with Excel)
   * - MINUS(value1, value2)
     - Difference of two numbers (not compatible with Excel)
   * - MULTIPLY(factor1, factor2)
     - Product of two numbers (not compatible with Excel)
   * - NE(value1, value2)
     - Not equal (not compatible with Excel)
   * - POW(base, exponent)
     - A number raised to a power (not compatible with Excel)
   * - UMINUS(value)
     - A number with the sign reversed (not compatible with Excel)
   * - UNARY.PERCENT(percentage)
     - Value interpreted as a percentage (not compatible with Excel)
   * - UPLUS(value)
     - A specified number, unchanged (not compatible with Excel)

.. _functions/statistical:

Statistical
===========

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - AVEDEV(value1, [value2, ...])
     - `Excel AVEDEV article <https://support.microsoft.com/office/avedev-function-58fe8d65-2a84-4dc7-8052-f3f87b5c6639>`_
   * - AVERAGE(value1, [value2, ...])
     - `Excel AVERAGE article <https://support.microsoft.com/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6>`_
   * - AVERAGE.WEIGHTED(values, weights, [additional_values, ...], [additional_weights, ...])
     - Weighted average (not compatible with Excel)
   * - AVERAGEA(value1, [value2, ...])
     - `Excel AVERAGEA article <https://support.microsoft.com/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091>`_
   * - AVERAGEIF(criteria_range, criterion, [average_range])
     - `Excel AVERAGEIF article <https://support.microsoft.com/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642>`_
   * - AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - `Excel AVERAGEIFS article <https://support.microsoft.com/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690>`_
   * - CORREL(data_y, data_x)
     - `Excel CORREL article <https://support.microsoft.com/office/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92>`_
   * - COUNT(value1, [value2, ...])
     - `Excel COUNT article <https://support.microsoft.com/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c>`_
   * - COUNTA(value1, [value2, ...])
     - `Excel COUNTA article <https://support.microsoft.com/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509>`_
   * - COVAR(data_y, data_x)
     - `Excel COVAR article <https://support.microsoft.com/office/covar-function-50479552-2c03-4daf-bd71-a5ab88b2db03>`_
   * - COVARIANCE.P(data_y, data_x)
     - `Excel COVARIANCE.P article <https://support.microsoft.com/office/covariance-p-function-6f0e1e6d-956d-4e4b-9943-cfef0bf9edfc>`_
   * - COVARIANCE.S(data_y, data_x)
     - `Excel COVARIANCE.S article <https://support.microsoft.com/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977>`_
   * - FORECAST(x, data_y, data_x)
     - `Excel FORECAST article <https://support.microsoft.com/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99>`_
   * - GROWTH(known_data_y, [known_data_x], [new_data_x], [b])
     - Fits points to exponential growth trend (not compatible with Excel)
   * - INTERCEPT(data_y, data_x)
     - `Excel INTERCEPT article <https://support.microsoft.com/office/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef>`_
   * - LARGE(data, n)
     - `Excel LARGE article <https://support.microsoft.com/office/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64>`_
   * - LINEST(data_y, [data_x], [calculate_b], [verbose])
     - `Excel LINEST article <https://support.microsoft.com/office/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d>`_
   * - LOGEST(data_y, [data_x], [calculate_b], [verbose])
     - `Excel LOGEST article <https://support.microsoft.com/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b>`_
   * - MATTHEWS(data_x, data_y)
     - Compute the Matthews correlation coefficient of a dataset (not compatible with Excel)
   * - MAX(value1, [value2, ...])
     - `Excel MAX article <https://support.microsoft.com/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098>`_
   * - MAXA(value1, [value2, ...])
     - `Excel MAXA article <https://support.microsoft.com/office/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d>`_
   * - MAXIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - `Excel MAXIFS article <https://support.microsoft.com/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883>`_
   * - MEDIAN(value1, [value2, ...])
     - `Excel MEDIAN article <https://support.microsoft.com/office/median-function-d0916313-4753-414c-8537-ce85bdd967d2>`_
   * - MIN(value1, [value2, ...])
     - `Excel MIN article <https://support.microsoft.com/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152>`_
   * - MINA(value1, [value2, ...])
     - `Excel MINA article <https://support.microsoft.com/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3>`_
   * - MINIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])
     - `Excel MINIFS article <https://support.microsoft.com/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599>`_
   * - PEARSON(data_y, data_x)
     - `Excel PEARSON article <https://support.microsoft.com/office/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18>`_
   * - PERCENTILE(data, percentile)
     - `Excel PERCENTILE article <https://support.microsoft.com/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba>`_
   * - PERCENTILE.EXC(data, percentile)
     - `Excel PERCENTILE.EXC article <https://support.microsoft.com/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314>`_
   * - PERCENTILE.INC(data, percentile)
     - `Excel PERCENTILE.INC article <https://support.microsoft.com/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed>`_
   * - POLYFIT.COEFFS(data_y, data_x, order, [intercept])
     - Compute the coefficients of polynomial regression of the dataset (not compatible with Excel)
   * - POLYFIT.FORECAST(x, data_y, data_x, order, [intercept])
     - Predict value by computing a polynomial regression of the dataset (not compatible with Excel)
   * - QUARTILE(data, quartile_number)
     - `Excel QUARTILE article <https://support.microsoft.com/office/quartile-function-93cf8f62-60cd-4fdb-8a92-8451041e1a2a>`_
   * - QUARTILE.EXC(data, quartile_number)
     - `Excel QUARTILE.EXC article <https://support.microsoft.com/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad>`_
   * - QUARTILE.INC(data, quartile_number)
     - `Excel QUARTILE.INC article <https://support.microsoft.com/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d>`_
   * - RANK(value, data, [is_ascending])
     - `Excel RANK article <https://support.microsoft.com/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723>`_
   * - RSQ(data_y, data_x)
     - `Excel RSQ article <https://support.microsoft.com/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f>`_
   * - SMALL(data, n)
     - `Excel SMALL article <https://support.microsoft.com/office/small-function-17da8222-7c82-42b2-961b-14c45384df07>`_
   * - SLOPE(data_y, data_x)
     - `Excel SLOPE article <https://support.microsoft.com/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9>`_
   * - SPEARMAN(data_y, data_x)
     - Compute the Spearman rank correlation coefficient of a dataset (not compatible with Excel)
   * - STDEV(value1, [value2, ...])
     - `Excel STDEV article <https://support.microsoft.com/office/stdev-function-51fecaaa-231e-4bbb-9230-33650a72c9b0>`_
   * - STDEV.P(value1, [value2, ...])
     - `Excel STDEV.P article <https://support.microsoft.com/office/stdev-p-function-6e917c05-31a0-496f-ade7-4f4e7462f285>`_
   * - STDEV.S(value1, [value2, ...])
     - `Excel STDEV.S article <https://support.microsoft.com/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23>`_
   * - STDEVA(value1, [value2, ...])
     - `Excel STDEVA article <https://support.microsoft.com/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d>`_
   * - STDEVP(value1, [value2, ...])
     - `Excel STDEVP article <https://support.microsoft.com/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195>`_
   * - STDEVPA(value1, [value2, ...])
     - `Excel STDEVPA article <https://support.microsoft.com/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c>`_
   * - STEYX(data_y, data_x)
     - `Excel STEYX article <https://support.microsoft.com/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab>`_
   * - TREND(known_data_y, [known_data_x], [new_data_x], [b])
     - Fits points to linear trend derived via least-squares (not compatible with Excel)
   * - VAR(value1, [value2, ...])
     - `Excel VAR article <https://support.microsoft.com/office/var-function-1f2b7ab2-954d-4e17-ba2c-9e58b15a7da2>`_
   * - VAR.P(value1, [value2, ...])
     - `Excel VAR.P article <https://support.microsoft.com/office/var-p-function-73d1285c-108c-4843-ba5d-a51f90656f3a>`_
   * - VAR.S(value1, [value2, ...])
     - `Excel VAR.S article <https://support.microsoft.com/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b>`_
   * - VARA(value1, [value2, ...])
     - `Excel VARA article <https://support.microsoft.com/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07>`_
   * - VARP(value1, [value2, ...])
     - `Excel VARP article <https://support.microsoft.com/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b>`_
   * - VARPA(value1, [value2, ...])
     - `Excel VARPA article <https://support.microsoft.com/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96>`_

.. _functions/text:

Text
====

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - CHAR(table_number)
     - `Excel CHAR article <https://support.microsoft.com/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a>`_
   * - CLEAN(text)
     - `Excel CLEAN article <https://support.microsoft.com/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41>`_
   * - CONCATENATE(string1, [string2, ...])
     - `Excel CONCATENATE article <https://support.microsoft.com/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d>`_
   * - EXACT(string1, string2)
     - `Excel EXACT article <https://support.microsoft.com/office/exact-function-d3087698-fc15-4a15-9631-12575cf29926>`_
   * - FIND(search_for, text_to_search, [starting_at])
     - `Excel FIND article <https://support.microsoft.com/office/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628>`_
   * - JOIN(delimiter, value_or_array1, [value_or_array2, ...])
     - Concatenates elements of arrays with delimiter (not compatible with Excel)
   * - LEFT(text, [number_of_characters])
     - `Excel LEFT article <https://support.microsoft.com/office/left-leftb-functions-9203d2d2-7960-479b-84c6-1ea52b99640c>`_
   * - LEN(text)
     - `Excel LEN article <https://support.microsoft.com/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb>`_
   * - LOWER(text)
     - `Excel LOWER article <https://support.microsoft.com/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4>`_
   * - MID(text, starting_at, extract_length)
     - `Excel MID article <https://support.microsoft.com/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028>`_
   * - PROPER(text_to_capitalize)
     - `Excel PROPER article <https://support.microsoft.com/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94>`_
   * - REPLACE(text, position, length, new_text)
     - `Excel REPLACE article <https://support.microsoft.com/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a>`_
   * - RIGHT(text, [number_of_characters])
     - `Excel RIGHT article <https://support.microsoft.com/office/right-rightb-functions-240267ee-9afa-4639-a02b-f19e1786cf2f>`_
   * - SEARCH(search_for, text_to_search, [starting_at])
     - `Excel SEARCH article <https://support.microsoft.com/office/search-searchb-functions-9ab04538-0e55-4719-a72e-b6f54513b495>`_
   * - SPLIT(text, delimiter, [split_by_each], [remove_empty_text])
     - `Excel TEXTSPLIT article <https://support.microsoft.com/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7>`_
   * - SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number])
     - `Excel SUBSTITUTE article <https://support.microsoft.com/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332>`_
   * - TEXT(number, format)
     - `Excel TEXT article <https://support.microsoft.com/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c>`_
   * - TEXTJOIN(delimiter, ignore_empty, text1, [text2, ...])
     - `Excel TEXTJOIN article <https://support.microsoft.com/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c>`_
   * - TRIM(text)
     - `Excel TRIM article <https://support.microsoft.com/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9>`_
   * - UPPER(text)
     - `Excel UPPER article <https://support.microsoft.com/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6>`_

.. _functions/web:

Web
===

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name and arguments
     - Description or link
   * - HYPERLINK(url, [link_label])
     - `Excel HYPERLINK article <https://support.microsoft.com/office/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f>`_

 
