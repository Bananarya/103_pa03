from transaction import transaction
import sys

"""Creat method to handle different activity"""
# def show_transaction():

#     if __name__=="__main__":
#         transact=transaction()
#         print("""
#             Welcome to the transaction sql interactive platform, please type the number to make a request:  
#             0. quit
#             4. show transactions
#             5. add transaction
#             6. delete transaction
#             7. summarize transactions by date
#             8. summarize transactions by month
#             9. summarize transactions by year
#             10. summarize transactions by category
#             11. print this menu
#             """)
#         action_num=int(input())
#         if(action_num==0):
#             print("Goodbye!")
#             return
#         elif(action_num==5):
#             print("Pleas tell me the information of the transaction you want to add")
#             item=input()
#         elif(action_num==6):
#             print("Pleas tell me the item #(rowid) of the transaction you want to delete")
#             rowid=input()


def print_usage():
    ''' print an explanation of how to use this command '''
    print("""
            Welcome to the transaction sql interactive platform, please type the number to make a request:  
            0. quit
            4. show transactions (show)
            5. add transaction (add)
            6. delete transaction (delete)
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize transactions by category
            11. print this menu
            """
            )

def print_todos(todos):
    ''' print the todo items '''
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-50s"%('item #','amount','category','date','description'))
    print('-'*40)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-10s %-10s %-50s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    todolist = transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todos = todolist.selectAll())
    elif arglist[0]=="showcomplete":
        print_todos(todolist.selectCompleted())
    elif arglist[0]=='add':
        print(arglist)
        if len(arglist)!=5:
            print_usage()
        else:
            todo = {'amount':arglist[1],'category':arglist[2],'date':arglist[3], 'description': arglist[4]}
            todolist.add(todo)
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = [] 
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1],args[2],args[3], " ".join(args[4:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()

