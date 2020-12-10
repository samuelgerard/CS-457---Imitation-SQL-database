import db_abstract
import db_module
import argparse
from PA2_test_run_script import test_string_list_PA2, test_string_list_PA3, test_string_list_PA4 
from arguments import arg_parser

EXIT_STATE = 'EXIT;'

argument_handler = arg_parser()

def start_db(commands = None, file = False):
    print('\n')
    choice = input('A PA_4 test run script is available.\nThis Script is an imitation of the PA_4_test.sql file. HOWEVER, because this iteration of the project is reliant on 2 command lines, this test file will only go up until after we begin a transaction and do the intial update to the flights table.\nWould you like to run it? (y/n):')
    if choice == 'y':
        print('\n')
        for com in test_string_list_PA4:
            # print(com)
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
    global argument_handler
    try: 
        if valid_input.upper() == EXIT_STATE:
            argument_handler.save()
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
