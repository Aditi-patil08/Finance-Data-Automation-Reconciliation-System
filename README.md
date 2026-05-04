#**Finance Data Automation \& Reconciliation System**

##** Objective**

Django-based finance data automation system with transaction reconciliation, REST APIs, and Power BI   dashboard insights.

##** Tech Stack**   \* Python  \* Django
  \* Django REST Framework  \* Power BI

##** Features**   
###** Data Ingestion**  
  &#x20;Bank statement and internal ledger data handled via Django Admin

##** Reconciliation Logic**  
\* Matches transactions based on:  
- &#x20; \* Exact amount matching  
- &#x20; \* Date difference ≤ 2 days  
- &#x20; \* Basic fuzzy matching on narration/description  


\# Ledger Automation  
\* Normalized ledger table with:    
- &#x20; \* Date  
- &#x20; \* Amount  
- &#x20; \* Category  
- &#x20; \* Source (bank/internal)  
- &#x20; \* Reconciliation status  

##**APIs**  
| Endpoint             | Description                                     |
| -------------------- | ----------------------------------------------- |
| /run-reconciliation/ | Executes reconciliation logic                   |
| /summary/            | Returns total credits, debits, unmatched amount |
| /reconciliation/     | Shows all processed transactions                |
| /category-breakdown/ | Expense grouped by category                     |


**
##\Dashboard (Power BI)**
- \* Expense by Category
- \* Daily Cashflow Trend
- \* Reconciliation Status
- \* KPI Cards (Total,Unmatched)

##** Sample Data**
Data was entered manually via Django Admin for testing.

##**Screenshots**
Screenshots of:
\* Admin panel
\* Data entry
\* API outputs
\* Dashboard
are available in the `screenshots/` folder.


##\ How to Run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  
--

Then open:
http://127.0.0.1:8000/admin/

#\ Author
Aditi Patil
