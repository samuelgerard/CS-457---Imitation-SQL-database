from arguments import db_runtime_context

class insert_argument(object):
    '''Models an INSERT statement'''
    def __init__(self, queryInput):
        '''
    	Purpose : Initialize an insert statement
    	Parameters : 
        	tableName: The name of the table to insert data into
            attrDataDict: A dictionary where the key / value pairs are the attribute
                          names and the corresponding data 
    	Returns: None
        '''
        self.__parseInsert(queryInput)

    def execute(self):
        ''' 
        Purpose : Execute an insert statement
        Parameters : 
            None
        Returns: None
        ''' 
        global db_runtime_context
        # table = db_runtime_context.current_db.tables[self.tableName]
        # if self.database is None:
        #     print ("!Failed to execute INSERT on table", self.tableName, "because no database is selected!")
        #     return 
        
        try:
            if self.tableName in db_runtime_context.current_db.tables:
                pass
            else:
                print ("!Failed to execute INSERT on table", self.tableName, "because it does not exist!")
                return

            # Check for a lock
            # if not self.database.isWritable(table.tableName):

            db_runtime_context.current_db.tables[self.tableName].insert(self.values)
            db_runtime_context.current_db.save()
            return
        except KeyError:
            print('KeyError!', self.tableName)
            return
        
        # self.database.successfulTransactions += 1

    def __parseInsert(self, queryInput):
        ''' 
        Purpose : Parse data to build an insert statement
        Parameters : 
            queryInput: Input to parse
        Returns: None
        ''' 
        tableName = queryInput[0] 
        
        # queryInput[1:] is now the values to insert. last value might have ) attached 
        queryInput = queryInput[1:]


        # Remove "values" and '(' from first element 
        queryInput[0] = queryInput[0][6:].replace('(', '')
        if(queryInput[0] == ''):
            queryInput = queryInput[1:] 
            
        values = []
        for i in range(len(queryInput)):
            temp = queryInput[i].replace(')', '').replace('(', '').strip().split(',')
            for val in temp:
                if val != '':
                    values.append(val.replace("'", ''))

        self.tableName = tableName.lower() # Sanitized table name 
        self.values = values # List of sanitized values to insert 


    
