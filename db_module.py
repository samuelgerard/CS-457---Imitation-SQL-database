import db_abstract
from db_abstract import objs as objs
import db_utility
import os



db_in_use = objs[0]


def db_create_table(table_args, columns):
    new_table_name = table_args[0]
    # pdb.set_trace()
    db_in_use.db_collection.append(db_in_use.db_table(new_table_name))

    if db_utility.check_empty_data_args(table_args[1:]):
        print('no datatype args to add, returning')
    
    db_in_use.db_collection[0].set_columns(columns)

    pass



def db_create(argument_list):
    argument_counter = db_utility.number_of_arguments(argument_list)
    argument_iterator = 0
    while(argument_iterator != argument_counter):
        if argument_list[argument_iterator] == 'table':
            pdb.set_trace()
            db_in_use.db_table(argument_list[argument_iterator+1])
            db_create_table(argument_list[1:], )
            return
        else:
            for same in objs:
                if same.db_name ==  argument_list[argument_iterator]:
                    print('that db already exist!')
                    return
            new_db = db_abstract._db_abstract_(argument_list[argument_iterator])
            db_abstract.objs.append(new_db)
            print('Database',argument_list[argument_iterator], 'has been created.')
            return


def db_delete_table(delete_table):
    counter = 0
    while(counter != len(db_in_use.db_collection)):
        if delete_table == db_in_use.db_collection[counter].db_table_name:
            del db_in_use.db_collection[counter]
            print('table', delete_table, 'deleted.')
            return
        counter = counter + 1
    print('that table does not exist.')
    return

def db_delete(delete_database):
    counter = 0
    while(counter != len(objs)):
        if delete_database == objs[counter].db_name:
            del objs[counter]
            print('db', delete_database, 'deleted.')
            return
        counter = counter + 1
    print('that db does not exist')

def db_set_current_db(current_db):
    # pdb.set_trace()
    for current in objs:
        if current.db_name == current_db:
            # pdb.set_trace()
            global db_in_use
            db_in_use = current
            return 
    print('Database does not exist. Please input an existing db')

if __name__ == "__main__":
    os.system('python main.py')