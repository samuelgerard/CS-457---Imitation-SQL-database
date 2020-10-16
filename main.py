import db_abstract
import db_module
import argparse
from PA2_test_run_script import test_string_list 
from arguments import arg_parser

EXIT_STATE = 'EXIT;'

def start_db(commands = None, file = False):
    print('\n')
    argument_handler = arg_parser()
    choice = input('A PA_2 test run script is available.\nThis Script is an imitation of the PA_2_test.sql file.\nWould you like to run it? (y/n):')
    if choice == 'y':
        print('\n')
        for com in test_string_list:
            parsed_arguments = argument_handler.parse_args(com)
        print('\nThe output of the test file is above')
        print('\n')
    elif choice == 'n':
        pass
        print('\n')
    else:
        pass        
        print('\n')      
    print('Type "?" for help')
    print('commands must end in a ";" to execute')
    while(True):
        try:
            user_arguments = input('>>> ')
            if valid_input(user_arguments):
                parsed_arguments = argument_handler.parse_args(user_arguments)    
            else:
                continue

        except KeyboardInterrupt:
            while(True):
                    y = input("Keyboard Interrupt, Exit Program? (y/n): ")
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
        elif not valid_input.endswith(';') or valid_input == "":
            return False
        elif valid_input.endswith(';'):
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
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional: Read in a sql script')
    parser.add_argument('input_file', help = 'a database of script file to create/manage any databases', nargs = '?')
    args = parser.parse_args()
    start_db()
