# 103_pa03 #
## transaction.py ##
### Demo: Rongzi Xie ###
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

### Test: Keer Xu ###
Keer Xu contributes to this project by creating the test_transaction.py file to test all methods in the transaction.py and make sure that all methods run correctly. 

## The following scripts are results by running tracker.py in terminal ##
 Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> show
no tasks to print
----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> add 20 food 2023/2/3 lunch
transaction added
----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> show
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> add 30 food 2023/2/4 dinner
transaction added
----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> add 10 food 2023/3/4 snack
transaction added
----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> show
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')
t=(2, 30, 'food', '2023/2/4', 'dinner', '2023', '2')
t=(3, 10, 'food', '2023/3/4', 'snack', '2023', '3')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

2          30         food       2023/2/4   dinner

3          10         food       2023/3/4   snack

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> std 2023/2/3
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> stm 2023/2
no tasks to print
----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> stm 2
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')
t=(2, 30, 'food', '2023/2/4', 'dinner', '2023', '2')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

2          30         food       2023/2/4   dinner

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> sty 2023
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')
t=(2, 30, 'food', '2023/2/4', 'dinner', '2023', '2')
t=(3, 10, 'food', '2023/3/4', 'snack', '2023', '3')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

2          30         food       2023/2/4   dinner

3          10         food       2023/3/4   snack

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> stc food
t=(1, 20, 'food', '2023/2/3', 'lunch', '2023', '2')
t=(2, 30, 'food', '2023/2/4', 'dinner', '2023', '2')
t=(3, 10, 'food', '2023/3/4', 'snack', '2023', '3')


item #     amount     category   date       description

----------------------------------------
1          20         food       2023/2/3   lunch

2          30         food       2023/2/4   dinner

3          10         food       2023/3/4   snack

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> p

            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

----------------------------------------




            Welcome to the transaction sql interactive platform, please type the command to make a request:
            q: quit
            show: show transactions
            add: add transaction
            delete: delete transaction
            std: summarize transactions by date
            stm: summarize transactions by month
            sty: summarize transactions by year
            stc: summarize transactions by category
            p: print this menu

command> q
