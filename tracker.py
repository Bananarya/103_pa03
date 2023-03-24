from transaction.py import transaction
"""Creat method to handle different activity"""
def show_transaction():

if __name__=="__main__":
        transact=transaction()
        print("""
            Welcome to the transaction sql interactive platform, please type the number to choose what action do you want:  
            0. quit
            4. show transactions
            5. add transaction
            6. delete transaction
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize transactions by category
            11. print this menu
            """)
        action_num=int(input())
        if(action_num==0):
            print("Goodbye!")
            return
        elif(action_num==5):
            print("Pleas tell me the information of the transaction you want to add")
            item=input()
        elif(action_num==6):
            print("Pleas tell me the item # of the transaction you want to add")
            rowid=input()
