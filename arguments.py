import db_module
import db_utility
import pdb
import os
from queue import Queue
from db_abstract import objs as objs
import db_context

db_runtime_context = db_context.db_context()

from Createmodule import create_argument

DEFAULT = 'EMPTY'


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
            "AVAILABLE": self.parseAvailable
        }

        #Notes for when I get back to this:
        #Parse the arguments into a string in a seperate function
        #return those arguments as a list of 'tokens'
        #make a seperate function to execute those commands
        
        input_string = input_string.strip() #strip whitespaces
        arguments = input_string.split('.') #split the argument string after the '.'
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
    
    #availble done
    #create database done
    #use done

    def parseAvailable(self, input):
        db_runtime_context.display_databases()

    def parseCreate(self, input):
        if input[0].upper() != "TABLE":
            initiate_create = create_argument("DATABASE", dbname=input[0])
            initiate_create.execute()
        elif input[0].upper() == "TABLE":
            create_argument("TABLE", attributes=input[1:])
        else:
            print('input unsuccesful')
            pass 

    def parseUse(self, input):
        db_runtime_context.set_database(input[0])
        pass

    def parseAlter(self, input):
        print('testing program 3')
        pass

    def parseDrop(self, input):
        print('testing program 4')
        pass

    def parseSelect(self, input):
        print('testing program 5')
        pass
    


    def parse_arguments(self,string_argument):
        #argument_counter = number_of_arguments(string_argument)
        list_of_arguments = []
        data_args = []
        argument_array = []

        try:
            for seek_argument in string_argument:
                if seek_argument == '?':
                    db_utility.options_display()
                    return
                elif seek_argument == ' ':
                    list_of_arguments.append(db_utility.list_to_string(argument_array))
                    argument_array = []
                    continue
                elif seek_argument == '.':
                    list_of_arguments.append(db_utility.list_to_string(argument_array))
                    break
                elif seek_argument == '(':
                    data_args = self.establish_data_args(string_argument)
                argument_array.append(seek_argument)
                

            
            if list_of_arguments[0] == 'create':
                if list_of_arguments[1] == 'table':
                    db_module.db_create_table(list_of_arguments[2:], data_args)
                else:
                    list_of_arguments = list_of_arguments[1:]
                    db_module.db_create(list_of_arguments)
            elif list_of_arguments[0] == 'delete':
                if list_of_arguments[1] == 'table':
                    db_module.db_delete_table(list_of_arguments[2])
                    return
                db_module.db_delete(list_of_arguments[1])
            elif list_of_arguments[0] == 'available':
                db_module.display_open_databases()
                return
            elif list_of_arguments[0] == 'use':
                db_module.db_set_current_db(list_of_arguments[1])
            elif list_of_arguments[0] == 'select':
                if list_of_arguments[1] == '*':
                    if list_of_arguments[2] == 'from':
                        counter = 0
                        while(True):
                            if db_module.db_in_use.db_collection[counter].db_table_name == list_of_arguments[3]:
                                db_module.db_in_use.db_collection[counter].display_columns()
                                return
                            if counter == 20:
                                 print('invalid search query')
                            counter = counter + 1    
                       
                    
            
            else:
                print('no proper arguments were validated')
                return 
        except ValueError:
            print('Argument parse error! please make sure your commands correctly. Returning to beginning command line.')
            return
        except KeyError:
            print('Key error, gotta fix this')
            return
        except IndexError:
            print("Index error, please ensure your command is correct and has a '.' at the end ")
        
        


if __name__ == "__main__":
    os.system('python main.py')