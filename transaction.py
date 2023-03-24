'''
transaction.py is an Object Relational Mapping to the transaction database

The ORM will work map SQL rows with the schema
    (item#,amount,category,date,description)
to Python Dictionaries as follows:

(5,5,'food',2023/3/24,'something to eat') <-->
{rowid:5,title:5,category:'food',date:2023/3/24,description:'something to eat')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transaction.db

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item#,amount, category,date,description), according to the demo, item# is the rowid'''
    print('t='+str(t))
    todo = {'item#':t[0], 'amount':t[1], 'category':t[2], 'date':t[3],'description':t[4]}
    return todo

class transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transaction
                    (amount int, category text, date text, description text)''',())
    
    def selectDate(self,date):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT item#,* from transaction where date="+date,())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT item#,* from transaction",())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO transaction VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM transaction WHERE item#=(?)",(rowid,))
    #not a useful method, but can be modified if u need
    """
    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE transaction SET completed=1 WHERE item#=(?)",(rowid,))
    """
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
if __name__=="__main__":
    transact=transaction()
