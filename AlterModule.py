from arguments import db_runtime_context

class alter_argument(object):
    def __init__(self, queryInput):
        self.queryInput = queryInput
        
    def execute(self):
        '''
        Purpose:    Implementation of the ALTER statement.  (Presently only has
                    ADD implemented to conform with PA1 requirements.
        Parameters: None
        Returns: None
        '''
        # Define states to execute correct helper function.
        states = {
            "ADD": self.__executeAdd,
            "DROP": self.__executeDrop,
            "MODIFY": self.__executeModify
        }

        # Fetch table name from SQL query.
        tableName = self.queryInput[0]

        # If the query is of sufficient length and uses a supported state,
        # call the helper function.
        if len(self.queryInput) > 1:
            state = self.queryInput[1].upper()
            if state in states.keys():
                states[state](tableName, self.queryInput[2:])
                print ("Table", tableName, "modified.")
            else:
                print ("!Invalid SQL Statement!")
        else:
            print ("!Invalid SQL Statement!")
    
    def __executeAdd(self, tableName, addInput):
        global db_runtime_context
        '''
        Purpose:    Private helper function to perform an ADD column.
        Parameters: None
        Returns: None
        '''
        if len(addInput) > 1:
            attributeName = addInput[0].strip()
            dataType = addInput[1].strip()
            if tableName in db_runtime_context.current_db.tables:
                db_runtime_context.current_db.tables[tableName].addColumn(attributeName, dataType)
            else:
                print('Invalid argument or table name.')
                
    def __executeDrop(self, dropInput):
        pass


    def __executeModify(self, modifyInput):
        pass
