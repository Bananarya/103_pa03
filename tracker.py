from transaction import transaction
import sys

"""Creat method to handle different activity"""

def print_usage():
    ''' print an explanation of how to use this command '''
    print("""
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
        values = values[:len(values)-2]
        print("%-10s %-10s %-10s %-10s %-50s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    todolist = transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todos = todolist.selectAll())
    elif arglist[0]=='add':
        if len(arglist)!=5:
            print_usage()
        else:
            todo = {'amount':arglist[1],'category':arglist[2],'date':arglist[3], 'description': arglist[4]}
            todolist.add(todo)
            print("transaction added")
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
            print("transaction deleted")
    elif arglist[0]=='std':
        if len(arglist)!=2:
            print_usage()
        else:
            print_todos(todos = todolist.selectDate(arglist[1]))
    elif arglist[0]=='stm':
        if len(arglist)!=2:
            print_usage()
        else:
            print_todos(todos = todolist.selectMonth(arglist[1]))
    elif arglist[0]=='sty':
        if len(arglist)!=2:
            print_usage()
        else:
            print_todos(todos = todolist.selectYear(arglist[1]))
    elif arglist[0]=='stc':
        if len(arglist)!=2:
            print_usage()
        else:
            print_todos(todos = todolist.selectCategory(arglist[1]))
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

