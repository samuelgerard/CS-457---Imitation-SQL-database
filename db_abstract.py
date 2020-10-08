#***database abstract class***
import numpy as np
import pdb

DEFAULT_NAME = 'EMPTY'

'''
    objs is a global variable that holds
    all of the current instances
    of table objects during runtime

'''


class _db_abstract_():


    class db_table():

        datatype_column = []
        element_row = []
        db_table_name = DEFAULT_NAME
        table_empty = True

        def __init__(self, db_name):
            self.db_table_name = db_name
        

        def set_columns(self, list_of_types):
            table_empty = False
            transfer = []
            counter = 0
            for data in list_of_types:
                if counter == 2:
                    self.datatype_column.append('|')
                    counter = counter + 1
                    continue
                self.datatype_column.append(data)
                counter = counter + 1
            print(' '.join(self.datatype_column))

        def display_columns(self):
            print(' '.join(self.datatype_column))

    def __init__(self, name):
        self.db_name = name
        self.tables = {}


DEFAULT_DB = _db_abstract_('default') #sets a default on runtime since there is no directory for stored databases yet
objs = [DEFAULT_DB]  #objs is a global list that stores the currently available databases for use
new_db_in_use = objs[0] 


