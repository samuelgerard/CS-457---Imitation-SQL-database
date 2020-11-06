DEFAULT_NAME = 'EMPTY'

import os
'''
    objs is a global variable that holds
    all of the current instances
    of table objects during runtime

'''


class _db_abstract_():


    def __init__(self, name):
        self.db_name = name
        self.tables = {}
    
    def addTable(self, newTable):
        if self.db_name is not None:
            self.tables[newTable.safeName] = newTable

    def save(self):
        '''
        Purpose:    Saves the Database and all member tables currently in
                    memory to the disk.  
        Parameters: None
        Returns: None
        '''
        # Call Table.save() for all tables in the database.
        for table in self.tables.values():
            table.save()
        
        # Delete all files no longer stored in the model 
        if self.db_name is not None:
            dbDir = "./" + self.db_name + "/"

            tableFiles = [tbl.fileName for tbl in self.tables.values()]
            # print(tableFiles)
            diskFiles = os.listdir(dbDir)
            for filename in diskFiles:
                if filename not in tableFiles:
                    os.remove(dbDir + filename)
    
        


DEFAULT_DB = _db_abstract_('default') #sets a default on runtime since there is no directory for stored databases yet
objs = [DEFAULT_DB]  #objs is a global list that stores the currently available databases for use
new_db_in_use = objs[0] 


