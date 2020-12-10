DEFAULT_NAME = 'EMPTY'

import os
import glob
from TableModule import Table

class _db_abstract_():


    def __init__(self, name):
        self.db_name = name
        self.tables = {}

        self.tranasactionInProgress = False
        self.successfulTransactions = 0

        # If we know the database name (i.e. it exists already) read in the
        # tables and add them to the Database object.
        if self.db_name is not None:
            tablesList = glob.glob(f"./{self.db_name}/*.tbl")
            for entry in tablesList:
                entry = entry.split("/")[-1]
                if entry.endswith(".tbl"):
                    entry = entry[0:-4]
                temp = Table(self.db_name, entry)
                #Strip off the .tbl extension 
                self.tables[temp.safeName] = temp 
    
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
    
    def isWritable(self, tableName):
        ''' 
        Purpose : Check if the given table is locked or not
        Parameters : 
            tableName: The table name to search for
        Returns: True if the table is writable; False otherwise
        ''' 
        # Check for a lock file 
        files = glob.glob(f"./{self.db_name}/{tableName}.*")
        if len(files) > 1:
            # Check the pid matches 
            pid = str(os.getpid())
            for filename in files:
                extension = filename.split('.')[2]
                if extension == pid:
                    return True 
            return False 
        return True

    def tableInDB(self, tableName):
        '''
        Purpose:    Boolean function to indicate if a given table is in the
                    database.
        Parameters: tableName: string name of the table to search for.
        Returns:    True if table is in the database, False if not.
        '''
        return (tableName.lower() in self.tables.keys())    
    
    def getTableByName(self, tableName):
        '''
        Purpose:    Retreives Table object by givent table name. 
        Parameters: tableName: string name of the table to return.
        Returns:    Correlated Table object for the given name.  None, if
                    table does not exist in the database.
        '''
        tableName = tableName.lower()
        if self.tableInDB(tableName):
            tname = self.tables[tableName].tableName 
            self.tables[tableName] = Table(self.db_name, tname)
            return self.tables[tableName]
        else:
            return None

        


DEFAULT_DB = _db_abstract_('default') #sets a default on runtime since there is no directory for stored databases yet
objs = [DEFAULT_DB]  #objs is a global list that stores the currently available databases for use
new_db_in_use = objs[0] 


