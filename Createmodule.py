import os
import pdb
import db_abstract
from TableModule import Table
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
        
        #reminder, check if the table already exist
        elif self.create_argument_type.upper() == "TABLE":
            new_table_name = self.attributes[0]
            if db_runtime_context is not None:
                table_schema = self.parseSchema(self.attributes[1:])
                new_table = Table(db_runtime_context.current_db.db_name, new_table_name, True)
                new_table.setSchema(table_schema)
                db_runtime_context.current_db.addTable(new_table)
                print('Table', new_table.tableName, 'created')

        else:
            print('invalid passed args.')

    
    def check_exist(self, input):
        global db_runtime_context
        for check_exist in db_runtime_context.database_archive:
            if check_exist.db_name == input:
                print('That database already exist!')
                return True
        return False

    def parseSchema(self,schemaInput):
        joined = " ".join(schemaInput).strip()
        if(joined.endswith(')')): joined = joined[:-1]
        if(joined.startswith('(')): joined = joined[1:]
        schemaVals = joined.split(',')
        schema = {}
        for val in schemaVals:
            val = val.strip().split()
            schema[val[0]] = val[1] 
        return schema

        