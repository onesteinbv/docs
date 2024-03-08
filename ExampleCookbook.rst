================================================
Example Cookbook
================================================

This document contains the actions which is required manually for pre and post migration specially for US DB.

**Table of contents**

.. contents::
   :local:

Server setup
================================================

As the server is sometimes a clone from an old instance, bring it up to date first.

Certificates
------------

.. code:: bash

  wget -q -O - http://gitlab.xx.lan/xxCA.crt > /usr/local/share/ca-certificates/xxCA.crt
  wget -q -O - http://gitlab.xx.lan/xxSSLCA.crt > /usr/local/share/ca-certificates/xxSSLCA.crt
  update-ca-certificates
  service docker restart

Update the odoo installation
----------------------------

.. code:: bash

  cd /opt/odoo/odoo13
  docker-compose down
  git pull
  docker-compose up -d

DB Setup
========
Download DB from GU server x.x.x.x
Restore the V8 DB on x.x.x.x server. (live)
Disable Emails.
Inactive Users(except admin) for V8 DB on x.x.x.x.(live)

Restore it on server x.x.x.x:8069.


Upload the V8 backup on x.x.x.x server for V8 UAT.

Configuration
================================================
Use migration scripts available at:
* https://gitlab.xx.lan/xx-odoo/openupgrade

Use Shell script for auto migration available at:
* https://gitlab.xx.lan/xx-odoo/migration-scripts

V8 to V9
========
* Nothing to do as steps are included in Shell Script.

V9 to V10
=========
* Nothing to do as steps are included in Shell Script.

V10 to V11
==========
* Nothing to do

V11 to V12
==========
* Nothing to do as steps are included in Shell Script.

V12 to v13
==========

Post-Migration
--------------

From http://x.x.x.x:8069/


QA To Configure
---------------
* company header and footer must be same as v8 in company configuration.

* Issue #0179 : Update sale and invoice email template 
  Update sale and invoice templates based on configuration done on UAT/IT.

* Uninstall Module

- gamification, hr_holidays, website, hr_attendance, hr_org_chart, sale_expense, xx_groups, account_payment_purchase, account_banking_mandate, xx_l10n_us_out_invoice_analysis
*others already removed from script.

* Install modules

- xx_report,xx_invoice,mapbox,xx_role_policy,xx_account_accruals, Extended Approval Sale order, Extended Approval Sales Target, xx_role_policy, web_environment_ribbon 


* Role Policy and URIM configuration 

Prerequisite :  xx_role_policy module install or not check
Download from UAT server and import

* URIM Configuration:
Key	xx_auth_db_id	Value	GU
Key	xx_auth_url	Value	http://xauth:nlFqOhfm6syOKRqK@x.x.x.x:28069/db_xx_rigtst_odoo

* Extended Approval flow Configuration

* Dropship Route

Inventory > Configuration > Route  
Configure Dropship same as 136 server
-Operation type in Rules wizard
-Reference configure 

* Remove user defined default

Users & Companies >  Users > 
Goto Settings > technical > User defined default : delete if action is not available.


* Account Dimension Policy Configuration
For Payable and receivable change Policy to "Optional”

Add the following analytic dimensions:
- Cost Center
- xx Campaign
- Project
- Operating Unit

* Record Rules

- Disable following record rules:
Pricelist versions from allowed operating units
Pricelists from allowed operating units
CRM Partner Action from allowed operating units
Account Type Multi Company rule

* Costing Method Configuration

Mass Editing:
Set 'Costing Method' to 'Average Cost' for all product categories containing storable products.

Set 'Inventory Valuation' and 'Account Stock Properties' same as in Odoo 8.0 for storable products.
(configuted inventory Valuation="Automated" for product category which we are configuring costing methid="Average cost")

* Shipping Method Configuration

Check and correct if needed.
- Open Porto Product
- Change Sale Description > Porto
- Sales > Configurations > Shipping method Name Remove (:) and duplicate name

* Report Layout

- We need to Set External Layout xx in Document Layout.

* Configure account type
1. Open Invoicing > Configuration
2. Select Account type
3. Click/open Payable and receivable
4. Change Analytic Dimensions > Policy to "Optional

* Session Expire
- In system parameter : inactive_session_time_out_delay	Value	7200

* Configure fiscal year

* Configure Company Logo 

* Date Ranges

- Create Date Range for current Fiscal Year
- Create Date Ranges for 12 Fiscal Periods (month)

* System Parameters

Update system parameter with key mail_thread_disable_auto_followers with Value ['sale.order', 'purchase.order', 'account.move']
Add system parameter web_m2x_options.create_edit as False
Add system parameter web_m2x_options.create as False
Add system parameter web_m2x_options.m2o_dialog as False

* Audit Trail

Configure Full Logs on the following objects:

- Bank accounts
- Sales Discounts
- Sales Discounts Rules
- Price Subcatalogs
- Price Catalog Items

Fix 'Any Product' on Marketing PO lines
---------------------------------------

cf. openupgrade purchase/migrations/9.0.1.2/post-migration.py, sale/migrations/9.0.1.0/post-migration.py :

Openupgrade creates product 'Any product' as follows

        product = env['product.product'].create({
            'name': 'Any product',
            'type': 'service',
            'order_policy': 'manual',
        })

and sets it to any purchase order line or sale order line when no product has been set in V8.

.. code:: sql

  SELECT pp.id FROM product_product pp
  JOIN product_template pt ON pp.product_tmpl_id = pt.id
  WHERE pt.name='Any product';
    id
  ------
   1580    (AP_ID)
  (1 row)

  SELECT COUNT(pol.id)
  FROM purchase_order_line pol
  JOIN purchase_order po ON pol.order_id=po.id
  WHERE pol.product_id=(AP_ID);
   count
  -------
   4223
  (1 row)

  SELECT COUNT(pol.id)
  FROM purchase_order_line pol
  JOIN purchase_order po ON pol.order_id=po.id
  WHERE pol.product_id=(AP_ID) AND po.xx_marketing=false;
   count
  -------
       5
  (1 row)

-> only marketing POs without product_id on POL.

.. code:: sql

  SELECT so.name, sol.id AS sol_id
  FROM sale_order_line sol
  JOIN sale_order so ON sol.order_id=so.id
  WHERE sol.product_id=(AP_ID);
     name   | sol_id
  ----------+--------
           ...
9130096 |    485
 9130045 |     61
 9130051 |    130
 9130051 |    131
 9130051 |    132
 9130054 |    164
 9130054 |    165


   (many rows)

Create product 'General Product' with settings:

- Name : General Product
- Flags : Can be purchased, Marketing, Modifiable prices
- Internal Reference : GP
- Product Type : Service
- Control Policy : On ordered quantities

.. code:: sql

  SELECT pp.id FROM product_product pp
  JOIN product_template pt ON pp.product_tmpl_id = pt.id
  WHERE pt.name='General Product';
    id
  ------
   1747    (GP_ID)
  (1 row)

  UPDATE purchase_order_line SET product_id=(GP_ID) WHERE product_id=(AP_ID);


Actions for Onsite team
-----------------------

* Operating Unit record rules

Newly created users don't receive a default_operating_unit_id and hence do not visibility on objects 
for which legacy operating unit record rules are not updated due to missing upgrade scripts.

This is the case for e.g. Journal Items (account.move.line).

Temporary bypass until final fix is available:

.. code:: sql

  select id, name, noupdate from ir_model_data where module='account_operating_unit' and model='ir.rule';
  update ir_model_data set noupdate=false where module='account_operating_unit' and model='ir.rule';

After this sql command the upgrade of the 'account_operating_unit' module restores the visibility on the
account.move.line objects.

* Via UI: upgrade base + check logging

Error during upgrade base: account.move.line constraint not set:

..code:: python

        (
            'check_amount_currency_balance_sign',
            '''CHECK(
                currency_id IS NULL
                OR
                company_currency_id IS NULL
                OR
                (
                    (currency_id != company_currency_id)
                    AND
                    (
                        (balance > 0 AND amount_currency > 0)
                        OR (balance <= 0 AND amount_currency <= 0)
                        OR (balance >= 0 AND amount_currency >= 0)
                    )
                )
            )''',
            "The amount expressed in the secondary currency must be positive when account is debited and negative when account is credited. Moreover, the currency field has to be left empty when the amount is expressed in the company currency."
        ),

Fixed via:

.. code:: sql

  SELECT id, date, currency_id, company_currency_id, balance, amount_currency, move_id
    FROM public.account_move_line
    WHERE NOT
      (
                currency_id IS NULL
                OR
                company_currency_id IS NULL
                OR
                (
                    (currency_id != company_currency_id)
                    AND
                    (
                        (balance > 0 AND amount_currency > 0)
                        OR (balance <= 0 AND amount_currency <= 0)
                        OR (balance >= 0 AND amount_currency >= 0)
                    )
                )
            )
  ORDER BY move_id, id;

--------+------------+-------------+---------------------+----------+-----------------+---------
   id    |    date    | currency_id | company_currency_id | balance  | amount_currency | move_id 
---------+------------+-------------+---------------------+----------+-----------------+---------
 1017518 | 2022-10-01 |           1 |                   3 | -1683.01 |         1683.01 |  248120
 1017519 | 2022-10-01 |           1 |                   3 |  1683.01 |        -1683.01 |  248120
 1034245 | 2023-01-01 |           1 |                   3 | -7287.82 |         7024.00 |  252797
 1034246 | 2023-01-01 |           1 |                   3 |  7287.82 |        -7024.00 |  252797
(4 rows)

Fix these entries: (*** This will be performed by on-site team (LDM) ***)

.. code:: sql

  UPDATE account_move_line SET amount_currency=-amount_currency WHERE id IN (1017518, 1017519, 1034245, 1034246);

New upgrade now sets the constraint.

* Tax configuration

Find taxes which have been used in the recent past:

.. code:: sql

  select distinct(rel.tax_id), at.name, at.type_tax_use from account_invoice_line_tax rel 
    join account_invoice_line ail on ail.id = rel.invoice_line_id
    join account_invoice ai on ai.id = ail.invoice_id
    join account_tax at on rel.tax_id = at.id
    where ai.date >= '2020-01-01'
    order by at.type_tax_use, rel.tax_id;

.. code::
 tax_id |          name           | type_tax_use 
--------+-------------------------+--------------
      3 | Exempted Tax (Purchase) | purchase
(1 row)

* Delete the no longer used account chart template :

.. code:: sql

  delete from account_fiscal_position_template;
  delete from account_tax_template;
  delete from account_account_template; 
  delete from account_chart_template;

  DELETE FROM ir_model_data
  WHERE model = 'account.fiscal.position.template' AND module='account';

  DELETE FROM ir_model_data
  WHERE model = 'account.tax.template' AND module='account';

  DELETE FROM ir_model_data
  WHERE model = 'account.account.template' AND module='account';

  DELETE FROM ir_model_data
  WHERE model = 'account.chart.template' AND module='account';

* Account Types (*** This will be performed by on-site team (LDM) ***)

Update the account types to match only account types with external ID starting with account.
Correct the chart of accounts to match only the new account types.

* Accounts

Create account 999999: type Current Year Earnings.Set this account to 'deprecated'.

8.0 closed accounts:

.. code:: sql

   update account_account set deprecated=true where openupgrade_legacy_9_0_type='closed';

8.0 inactive accounts:

.. code:: sql

   update account_account set deprecated=true where active=false;


8.0 (copy) accounts

.. code:: sql

  select id from account_account where code like '%(copy)';
 id  
-----
 480
 481
 483
 494
 495
 496
 497
 498
(8 rows)

 
(0 rows)

  select id from account_move_line where account_id in(select id from account_account where code like '%(copy)');
   id 
  ----
  (0 rows)

  delete from account_account where id in (select id from account_account where code like '%(copy)');


* Payment Methods

The OpenUpgrade scripts have set account.payment,payment_method_id to wrong payment methods.
We only want to keep Manual for Inbound & Outbound, keep Electronic for Inbound and keep SEPA Credit Transfer v03 (recommended). Keeping SEPA Credit Transfer is for future use since no Payment Orders are used at this point in time.

select id, name, payment_type from account_payment_method order by id;
.. code:: sql

 id |                          name                          | payment_type 
----+--------------------------------------------------------+--------------
  1 | Manual                                                 | inbound
  2 | Manual                                                 | outbound
  3 | SEPA Direct Debit v02 (recommended)                    | inbound
  4 | SEPA Direct Debit v03                                  | inbound
  5 | SEPA Direct Debit v04                                  | inbound
  6 | SEPA Credit Transfer v05                               | outbound
  7 | SEPA Credit Transfer v04                               | outbound
  8 | SEPA Credit Transfer v03 (recommended)                 | outbound
  9 | SEPA Credit Transfer v02                               | outbound
 10 | SEPA Credit Transfer pain 001.003.03 (used in Germany) | outbound
 11 | Electronic                                             | inbound
(11 rows) 


.. code:: sql

  update account_payment set payment_method_id = 1 where payment_type = 'inbound';
  update account_payment set payment_method_id = 2 where payment_type = 'outbound';
  delete from account_payment_method where id in (3,4,5,6,7,9,10);

Reconfigure SEPA Credit Transfer v03 (recommended):
- Change Code to sepa_credit_transfer
- Pain = pain.001.001.03 (recommended for credit transfer)

* Payment Modes



* Journals

- Archive the Sales Refund & Purchase Refund Journals
- Check the sequences and configure when required
- Update the bank journals with the correct payment methods  no SEPA CT for cash & credit card journals(Need verification)
- Check Register Payment Button Settings on the Bank journals => All booleans should be false
- Create Exchange Rate Journal. Add 910210 Currency Difference account to Default Debit Account and Default Credit Account

* General Settings > Invoicing

- Tick the option Multi-Currencies
- Add the Exchange Rate journal to Exchange Gain or Loss Journal box.

* Mass Editing 

- Create a Mass Editing option and call it Update Lock Date. Model = Journal. Field = Lock Date. Add sidebar button. (Not Performed yet)

* Set legacy accounts to deprecated

.. code:: sql

  update account_account set deprecated = true where code like 'L%'; 
   id 
----
 14
 43
  6
 61
 69
 70
 71
 74
 77
 78
 80
(11 rows)


Via UI: set type 'Current Assets' for legacy account L-120010, set type 'Current Liabilities' for legacy account L-200010

* FIX incorrect Journal Entry naming for draft & cancelled supplier invoices 

.. code:: sql

  update account_move
    set name = '/'
    where state in ('draft', 'cancel')
      and type = 'in_invoice'
      and journal_id = 3
      and (create_date is null or create_date < '2023-04-17') /* created by OpenUpgrade */
      and name != '/';

  UPDATE 12

run invoice line repair script (Not Performed Yet- LDM to perform)

install xx_repair_mig13_invoice_lines module

Find out DB migration timestamp:
SELECT create_date FROM ir_module_module WHERE name = 'role_policy';

        create_date
----------------------------
 2023-04-12 10:26:18.548007

Find out highest account_move_line ID in the 8.0 database so that the migration
wizard can remove faulty accounting entries created by OpenUpgrade.

Remark: running the below query on the 13.0 database will result in a completely corrupted database !!

SELECT id, create_date FROM account_move_line
WHERE create_date < '%s' ORDER BY id DESC LIMIT 1;
   id    |        create_date
---------+----------------------------
 1042716 | 2023-04-12 03:24:43.828889
%s is the timestamp of the db migration.

run repair wizard
uninstall xx_repair_mig13_invoice_lines module

NOT DONE YET ON UAT:
------------------- 

* Clean-up legacy accounting entries

.. code:: sql

  update account_account set deprecated = false where code like 'L%'; (Not performed Yet)

Create misc journal entries to set all balances to 0.00 per FY end on Fiscal Years with
accounting entries on legacy accounts.

.. code:: sql

  update account_account set deprecated = true where code like 'L%'; (Not performed Yet)


Post migration (connecting tools and software) (No need to perfom at UAT- only when do production)
================================================

After migration of odoo, some other software tools which connect to odoo have to be reconfigured.

**Only perform these steps after the migrated database is LIVE. The external tools have 
to be connected to the live database at all times.**

EDI
---

Action has to be performed by IntoData, they have to reconfigure the talend server,
which polls odoo.

Provide them with:

- the new ip address of the server
- the database name (if changed)

All other settings they require remain unchanged.

BI tool -Done
-------

Follow the instructions on https://gitlab.xx.lan/xx-odoo/scripts-c2c#upgrade to upgrade
the BI tool to the latest version.

Because the new servers are usually clones of different entities, make double sure the config
file for the BI tool is the config file for the correct entity.

Adjust the config file (typically /home/xxreporting/xx/copy_report_data.config.sh) for V13:

.. code::

  #!/bin/bash
  LOCAL_DB=gu_xx
  VERSION="13"


Request Smoose to update the BI proxy settings to point to the new server ip.


Corporate BI tool
-----------------

The corporate BI tool for the group (xx or hortisol) to which the entity belongs also has to 
be adjuste

Log in to the applicable corporate BI server, and adjust the copy_report_data.config.<ENTITY>.sh

.. code:: bash

  #!/bin/bash

  VERSION="13"

  LOCAL_DB=gu_xx
  LOCAL_DB_HOST=x.x.x.x
  LOCAL_COMPOSE="/opt/odoo/odoo13/docker-compose.yml"
  LOCAL_ENV="/opt/odoo/odoo13/.env"

  ALL="1"
  LOCALCUR="1"
  CONSOLIDATED="1"
  DENORMALIZE="0"


Pivot- Done 
-----

To convert the pivot to the new database, change the config inside the script

.. code:: bash

  ssh <user>@x.x.x.x
  pico /opt/scripts/pivots/management/finance/finance8.py
    
here you will find configuration similar to:

.. code:: python

  pivot_db_config = [
    ## SKIP

    {
      'host': 'x.x.x.x',
      'db_name': 'db_xx_us_odoo',
      'query_extra': "WHERE date >= '2013-01-01'"
    },
    ## SKIP
  ]

comment this section and add an equivalent section lower:

.. code:: python

  pivot13_db_config = [
    ## SKIP
    {
     'host': 'x.x.x.x',
     'db_name': 'us_xx',
     'query_extra': "WHERE date >= '2013-01-01'"
    },
  ]


