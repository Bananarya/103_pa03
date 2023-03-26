import unittest
import sqlite3
import os
from datetime import datetime

from transaction import transaction

# this test is written by Keer Xu
class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        self.transaction = transaction()
        self.transaction.runQuery('''CREATE TABLE IF NOT EXISTS transaction_table
                                    (amount int, category text, date text, description text, year text, month text)''',())

    def test_add_delete_and_select(self):
        item = {'amount': 50, 'category': 'food', 'date': '2023/3/26', 
                'description': 'Lunch'}
        item1 = {'amount': 20, 'category': 'food', 'date': '2023/2/26', 
                'description': 'Dinner'}
        self.transaction.add(item)
        self.transaction.add(item1)
        result = self.transaction.selectDate('2023/3/26')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 50)
        self.assertEqual(result[0]['category'], 'food')
        self.assertEqual(result[0]['description'], 'Lunch')
        result1 = self.transaction.selectDate('2023/2/26')
        self.assertEqual(len(result1), 1)
        self.assertEqual(result1[0]['amount'], 20)
        self.assertEqual(result1[0]['category'], 'food')
        self.assertEqual(result1[0]['description'], 'Dinner')
        self.transaction.delete(1)
        self.transaction.delete(2)


    def test_select_all(self):
        item = {'amount': 50, 'category': 'cloth', 'date': '2023/3/26', 
                'description': 'new_cloth'}
        item1 = {'amount': 20, 'category': 'food', 'date': '2023/2/26', 
                'description': 'Dinner'}
        self.transaction.add(item)
        self.transaction.add(item1)
        result = self.transaction.selectAll()
        self.assertEqual(len(result), 2)
        self.transaction.delete(1)
        self.transaction.delete(2)

    def test_select_category(self):
        item = {'amount': 50, 'category': 'cloth', 'date': '2023/3/26', 
                'description': 'new_cloth'}
        item_same_date1 = {'amount': 20, 'category': 'food', 'date': '2023/2/26', 
                'description': 'Dinner'}
        item_same_date2 = {'amount': 30, 'category': 'food', 'date': '2023/3/26', 
                'description': 'Dinner'}
        self.transaction.add(item)
        self.transaction.add(item_same_date1)
        self.transaction.add(item_same_date2)
        result = self.transaction.selectCategory('food')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], 20)
        self.assertEqual(result[1]['amount'], 30)
        self.transaction.delete(1)
        self.transaction.delete(2)
        self.transaction.delete(3)

    def test_select_mon_year(self):
        item = {'amount': 50, 'category': 'cloth', 'date': '2023/3/26', 
                'description': 'new_cloth'}
        item_same_date1 = {'amount': 20, 'category': 'food', 'date': '2022/2/26', 
                'description': 'Dinner'}
        item_same_date2 = {'amount': 30, 'category': 'food', 'date': '2023/2/26', 
                'description': 'Dinner'}
        self.transaction.add(item)
        self.transaction.add(item_same_date1)
        self.transaction.add(item_same_date2)
        result_feb = self.transaction.selectMonth(2)
        self.assertEqual(len(result_feb), 2)
        self.assertEqual(result_feb[0]['amount'], 20)
        self.assertEqual(result_feb[1]['amount'], 30)
        result_23 = self.transaction.selectYear(2023)
        self.assertEqual(len(result_23), 2)
        self.assertEqual(result_23[0]['amount'], 50)
        self.assertEqual(result_23[1]['amount'], 30)
        self.transaction.delete(1)
        self.transaction.delete(2)
        self.transaction.delete(3)

if __name__ == '__main__':
    unittest.main()
