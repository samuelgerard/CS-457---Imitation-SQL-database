import os
import pdb
import db_abstract
from arguments import db_runtime_context


class create_argument:
    '''
    create argument class for handling the creation of new databases or tables.
    By default a newly created database will be the one that is set in use.
    '''
    def __init__(self, create_argument_type, dbname = None, attributes = None):
        self.create_argument_type = create_argument_type
        self.dbname = dbname
        self.attributes = attributes
    
    def execute(self):
        global db_runtime_context
        if self.check_exist(self.dbname):
            return
        if self.create_argument_type.upper() == "DATABASE":
            new_database = db_abstract._db_abstract_(self.dbname)
            db_runtime_context.add_database_to_archive(new_database)
            db_runtime_context.current_db = new_database
            print('New database', db_runtime_context.current_db.db_name,'successfully created')
        
        #elif self.create_argument_type.upper() == "TABLE":
    
    def check_exist(self, input):
        global db_runtime_context
        for check_exist in db_runtime_context.database_archive:
            if check_exist.db_name == input:
                print('That database already exist!')
                return True
        return False
        