'''
transaction.py is an Object Relational Mapping to the transaction database

The ORM will work map SQL rows with the schema
    (item#,amount,category,date,description)
to Python Dictionaries as follows:

(5,5,'food',2023/3/24,'something to eat') <-->
{rowid:5,title:5,category:'food',date:2023/3/24,description:'something to eat')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transaction.db
Author: Rongzi Xie
Editor: James Ma, Liulu Yue

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item#,amount, category,date,description), according to the demo, item# is the rowid'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3],'description':t[4],'year':t[5],'month':t[6]}
    return todo
#Rongzi Xie
class transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transaction_table
                    (amount int, category text, date text, description text, year text, month text)''',())
    
    def selectDate(self,date):  
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transaction_table where date=(?)",(date,))

    def selectCategory(self,category):
        return self.runQuery("SELECT rowid,* from transaction_table where category=(?)",(category,))

    def selectMonth(self,month):
        return self.runQuery("SELECT rowid,* from transaction_table where month=(?)",(month,))

    def selectYear(self,year):
        return self.runQuery("SELECT rowid,* from transaction_table where year=(?)",(year,))

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transaction_table",())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        date = item['date'].split('/')
        year = date[0]
        month = date[1]
        return self.runQuery("INSERT INTO transaction_table VALUES(?,?,?,?,?,?)",(item['amount'],item['category'],item['date'],item['description'],year,month))
        
    def delete(self,rowid):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM transaction_table WHERE rowid=(?)",(rowid,))
    #not a useful method, but can be modified if u need
    """
    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE transaction_table SET completed=1 WHERE rowid=(?)",(rowid,))
    """
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/transaction1.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
if __name__=="__main__":
    transact=transaction()
