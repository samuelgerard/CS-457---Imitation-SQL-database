from arguments import db_runtime_context

class delete_argument:
    def __init__(self, queryInput):
        self.tableName, self.conditions = self.__parseDelete(queryInput)

    def execute(self):
        ''' 
        Purpose : Execute a delete statement
        Parameters : 
            None
        Returns: None
        ''' 
        global db_runtime_context

        if self.tableName not in db_runtime_context.current_db.tables:
            print("!Failed to delete from table", self.tableName, "because table does not exist!")
            return None

        # Check for a lock
        # if not self.database.isWritable(table.tableName):
        #     print(f"Error: Table {table.tableName} is locked!")
        #     return

        db_runtime_context.current_db.tables[self.tableName].delete(self.conditions)

        # self.database.successfulTransactions += 1

    def __parseDelete(self, queryInput):
        ''' 
        Purpose : Parse input to build a delete statement
        Parameters : 
            queryInput: The input to parse
        Returns: tablename, conditions
        ''' 
        tableName = queryInput[0].lower()
        conditions = queryInput[2:]

        return tableName, conditions