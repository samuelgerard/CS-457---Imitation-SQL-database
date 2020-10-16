import db_module
import db_utility
import pdb
import os
from queue import Queue
from db_abstract import objs as objs
import db_context

db_runtime_context = db_context.db_context()
DEFAULT = 'EMPTY'

from Createmodule import create_argument
from SelectModule import select_argument
from AlterModule import alter_argument
from InsertModule import insert_argument
from UpdateModule import update_argument    
from DeleteModule import delete_argument


class arg_parser():

    arguments_to_parse = DEFAULT
    
    def __init__(self):
        self.arguments = Queue()

    def valid_command(self, command_string):
        pass

    def number_of_arguments(self,string_argument):
        return len(string_argument.split()) 

    def establish_data_args(self, args_string):
        new_list = db_utility.string_to_list(args_string)
        data_list = db_utility.handle_parenthesis(new_list[3:])

        return data_list  
    
    def parse_args(self, input_string):

        states = {
            "CREATE": self.parseCreate,
            "USE": self.parseUse,
            "ALTER": self.parseAlter,
            "DROP": self.parseDrop,
            "SELECT": self.parseSelect,
            "AVAILABLE": self.parseAvailable,
            "UPDATE": self.parseUpdate,
            "INSERT": self.parseInsert,
            "ALL": self.display_all,
            "DELETE": self.parseDelete
        }

        #Notes for when I get back to this:
        #Parse the arguments into a string in a seperate function
        #return those arguments as a list of 'tokens'
        #make a seperate function to execute those commands

        #ALL DONE
        
        input_string = input_string.strip() #strip whitespaces
        arguments = input_string.split(';') #split the argument string after the ';'
        iteration = 0
        for check_states in arguments:
            check_states = check_states.strip()
            if check_states == "?":
                db_utility.options_display()
                return
            if check_states == "":
                continue
            token_args = check_states.split()
            if token_args[0].upper() in states.keys():
                self.arguments.put(states[token_args[0].upper()](token_args[1:]))
        return self.arguments


    def parseAvailable(self, input):
        db_runtime_context.display_databases()

    def parseCreate(self, input):
        if input[0].upper() == "DATABASE":
            initiate_create = create_argument("DATABASE", dbname=input[1])
            initiate_create.execute()
        elif input[0].upper() == "TABLE":
            initiate_create_table = create_argument("TABLE", attributes=input[1:])
            initiate_create_table.execute()
        else:
            print('input unsuccesful')
            pass 

    def parseUse(self, input):
        db_runtime_context.set_database(input[0])


    def parseAlter(self, input):
        if input[0].upper() == "TABLE":
            initiate_alteration = alter_argument(input[1:])
            initiate_alteration.execute()
        else:
            return None

    def parseDrop(self, input):
        if input[0].upper() == "DATABASE":
            db_runtime_context.delete_database(input[1])
        elif input[0].upper() == "TABLE":
            db_runtime_context.delete_table(input[1])
        else:
            print('nothing')
    
    def parseInsert(self, input):
        if input[0].upper() != "INTO":
            print('Invalid statement!')
            return None
        initiate_insert = insert_argument(input[1:])
        initiate_insert.execute()

    def parseUpdate(self, input):
        initiate_update = update_argument(input)
        initiate_update.execute()
        
    def display_all(self, input):
        db_runtime_context.display_all_tables()


    def parseSelect(self, input):
        select_parse = select_argument(input)
        select_parse.execute()
    
    def parseDelete(self, input):
        initiate_delete = delete_argument(input[1:])
        initiate_delete.execute()    
        


if __name__ == "__main__":
    os.system('python main.py')