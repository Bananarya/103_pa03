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
## tracker.py: Liulu Yue && James Ma ##
tracker.py is an app that maintians a financial transactions history. It is meant to be used as a shell command. <br />
This app will store all transactions in a SQLite database ~/transaction1.db. <br />
Once start, this app will ask for input command, process your command, and print the menu to prompt for another command until nothing is entered or the user want to quit the app voluntarily by entering q. <br />
Supported commands are:
- q: quit <br />
	Typing q will exit from the app.
- show: show transactions <br />
    show all the transactions in the database
- add: add transaction <br />
    add transaction in the format of (amount, catagory, date(YYYY/MM/DD), description)
- delete: delete transaction <br />
    delete a transaction specifying the item #
- std: summarize transactions by date <br />
	Typing std followed by a specific date will give you all transactions on that date.
- stm: summarize transactions by month <br />
	Typing stm followed by the month (number) will give you all transactions in the specified month.
- sty: summarize transactions by year <br />
	Typing sty followed by the year (number) will give you all transactions in the specified year.
- stc: summarize transactions by category <br />
	Typing stc followed by category will give you all transactions with the specified category. <br />
(std, stm, sty, and stc each takes only one input except command itself. If the input length is not desired length, illegal argument will be printed. Please try again with correct format input.)
- p: print the menu <br />
	Typing p will show the menu of all supported commands. 


### Test: Keer Xu ###
Keer Xu contributes to this project by creating the test_transaction.py file to test all methods in the transaction.py and make sure that all methods run correctly. 

## The following scripts are results by running pylint on tracker.py and transaction.py ##

************* Module transaction
transaction.py:59:86: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:27:0: C0103: Class name "transaction" doesn't conform to PascalCase naming style (invalid-name)
transaction.py:64:29: W0622: Redefining built-in 'tuple' (redefined-builtin)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 8.89/10, +0.28)

************* Module tracker
tracker.py:9:0: C0301: Line too long (108/100) (line-too-long)
tracker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tracker.py:55:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:61:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:80:12: W0702: No exception type(s) specified (bare-except)
tracker.py:64:0: R0912: Too many branches (23/12) (too-many-branches)
tracker.py:124:12: R1723: Unnecessary "else" after "break", remove the "else" and de-indent the code inside it (no-else-break)

------------------------------------------------------------------
Your code has been rated at 9.00/10 (previous run: 7.89/10, +1.11)

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
