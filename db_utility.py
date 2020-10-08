import db_abstract
from db_abstract import objs as objs
import db_utility
import os
import pdb
from db_abstract import new_db_in_use

'''
    database utility functions
'''
def display_open_databases():
    global new_db_in_use
    print('Available databases:')
    for display in db_abstract.objs:
        if display.db_name == 'default':
            continue
        print(display.db_name, sep = ' ')
    print('Current database in use:', new_db_in_use.db_name)

def db_set_current_db(current_db):
    global objs
    for current in objs:
        if current.db_name == current_db:
            global new_db_in_use
            new_db_in_use = current
            return 
    print('Database does not exist. Please input an existing db')


def check_empty_data_args(passed_list):
    if not passed_list:
        return True
    return False

def list_to_string(passed_list):
    string = ""
    return(string.join(passed_list))

def string_to_list(passed_list):
    li = list(passed_list.split(" ")) 
    return li 

def handle_parenthesis(passed_list):
    stack_handle = 0
    finished = 0
    clean_list = []  
    for a in passed_list:
        for b in list(a):
            if b == '(' and stack_handle == 0:
                clean_list.append(a.replace('(',''))
                stack_handle = stack_handle + 1
                finished = finished + 1
                break
            elif b == ',':
                clean_list.append(a.replace(',',''))
                finished = finished + 1
                break
        if finished == 1:
            finished = 0
            continue
        elif finished == 0:
            clean_list.append(a)    
            
    return clean_list 
    

def number_of_arguments(string_argument):
    return len(string_argument) 

def options_display():
    print("*****************************************************")
    print("create --name_of_database\ndelete --name_of_database/table --name_of_table\navailable --shows what databases are currently running\navailable --prompt available databases and the currently used database \nSelect --* --from --name_of_table\n'Keyboard Interrupt' anytime to prompt for program exit\n ")
    print("*****************************************************")

def live_indicator():
    print(">> ", end = "")

def arg_is_true(arg):
    if(arg == False):
        return False
    else:
        return True