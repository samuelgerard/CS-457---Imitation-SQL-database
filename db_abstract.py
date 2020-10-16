DEFAULT_NAME = 'EMPTY'

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
    
        


DEFAULT_DB = _db_abstract_('default') #sets a default on runtime since there is no directory for stored databases yet
objs = [DEFAULT_DB]  #objs is a global list that stores the currently available databases for use
new_db_in_use = objs[0] 


