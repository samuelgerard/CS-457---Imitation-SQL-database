import pdb
import db_abstract
import db_module
import argparse
from arguments import arg_parser

EXIT_STATE = 'EXIT.'

def start_db():
    print('Type "?" for help')
    print('commands must end in a "." to execute')
    print('If you did not read the documentation yet. PLEASE read it before handling this program.')
    while(True):
        argument_handler = arg_parser()
        try:
            user_arguments = input('>>> ')
            if valid_input(user_arguments):
                parsed_arguments = argument_handler.parse_args(user_arguments)    
            else:
                continue

        except KeyboardInterrupt:
            while(True):
                    y = input("Keybaord Interrupt, Exit Program? (y/n): ")
                    if y == 'n':
                        continue
                    elif y == 'y':
                        exit()
                    else:
                        print("Invalid input\n")            
        except ValueError:
                print("Invalid Value Input")
                continue

def valid_input(valid_input):
    try: 
        if valid_input.upper() == EXIT_STATE:
            print('session complete, goodbye!')
            exit()
        elif not valid_input.endswith('.') or valid_input == "":
            return False
        elif valid_input.endswith('.'):
            return True
        else:
            print('Value error')
            return False 
    except EOFError:
        print('EOF error')
        exit()
    except ValueError:
        print('Value error!')
        return False

# def execute_instructions(execute_instructions):
#     print('executing instructions')
#     while not execute_instructions.empty():
#         execute_instructions.get()


        #come back here to deal with the current database context and use statement

        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional: Read in a sql script')
    parser.add_argument('input_file', help = 'a database of script file to create/manage any databases', nargs = '?')
    args = parser.parse_args()
    start_db()
