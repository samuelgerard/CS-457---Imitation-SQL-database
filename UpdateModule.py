import re
from arguments import db_runtime_context

class update_argument(object):
    def __init__(self, queryInput):
        self.database = None
        self.tableName, self.targets, self.conditions = self.__parseUpdate(queryInput) 

    def execute(self):
        """
        When we execute the an update command. We first check to ensure that there is actually
        a database and not a NoneType. We then lower case enforce the tableName so we can find 
        the table by it's name in the arrangement of tables in the database. If that table in
        the database is currently under a transaction, the execute will be cancelled. Otherwise,
        we update the table with the targets and indicated conditions. We then append successful
        transactions to +1.

        """
        global db_runtime_context
        if db_runtime_context.current_db is None:
            print("!Failed to execute query because no database is selected!")
            return None 

        self.tableName = self.tableName.lower()
        
        if self.tableName is not None:

            update_table = db_runtime_context.current_db.getTableByName(self.tableName)

            if update_table is not None:
                pass
            else:
                print("!Failed to execute query on table", self.tableName, "because it does not exist!")
                return None 

            # Check for a lock
            if not db_runtime_context.current_db.isWritable(update_table.tableName):
                print(f"Error: Table {update_table.tableName} is locked!")
                return



            db_runtime_context.current_db.tables[self.tableName].update(self.targets, self.conditions)

            db_runtime_context.current_db.successfulTransactions += 1


    def __parseUpdate(self, queryInput):

        tableName = queryInput[0] 

        if queryInput[1].lower() != "set":
            print ("!Invalid SQL statement!")
            return None, None, None 
        
        # Join the input into a string so it can be manipulated more easily
        joinStr = ' '.join(queryInput[2:]) 
        splitJoin = re.split("where", joinStr, flags=re.IGNORECASE)

        updates = {}
        conditions = None

        # Parse out the required bits of the statement 
        updatesSplit = re.split("=|,", splitJoin[0])
        if len(updatesSplit) < 2:
            print ("!Invalid SQL Statement!")
            return None, None, None,
        
        for i in range(0, len(updatesSplit), 2):
            try: 
                col = updatesSplit[i].strip().replace("'", '')
                val = updatesSplit[i + 1].strip().replace("'", '')
                updates[col] = val 
            except:
                print ("!Invalid SQL statement!")
                return None, None, None 
        # Check for a where clause 
        if len(splitJoin) > 1:
            conditions = list(filter(None, re.split(r"(=|!=|<>|<|>|<=|>=)", splitJoin[1])))
            conditions = [x.strip().replace("'", '') for x in conditions]
        
        return tableName, updates, conditions