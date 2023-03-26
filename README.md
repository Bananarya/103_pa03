# 103_pa03 #
## transaction.py ##
### Demo: Rongzi Xie ###
As the starter of this PA, I create a demo of transaction.py which conatins some basic method of creating and modifying the table of transaction using sql. The basic method including adding and deleting method and some functions about selecting items which have same properties like date.
toDict(t): Change the output of sql table to a dictionary which contained all the information of columns and th ename of each column as key.
__init__: run the runQuery method to crate a database containd the amount category date and description of an item

selectDate(date): Select certain items with same datte

selectMonth(month): Select certain items with same month

selectCategory(category): Select certain items with same category

selectYear(year): Select certain items with same Year

selectAll(): Select all the items in the sql table

add(item): add an item with all the information the sql table need

delete(rowid): delete the item by its rowid

runQuery(query,tuple): create a sql table and return all the items as dictionaries.
## tracker.py ##
### Demo: Rongzi Xie ###
Simple starter code of structure: Providing output to the user and get input from user for their inquery and details.

### Test: Keer Xu ###
Keer Xu contributes to this project by creating the test_transaction.py file to test all methods in the transaction.py and make sure that all methods run correctly. 
