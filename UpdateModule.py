import re
from arguments import db_runtime_context

class update_argument(object):
    def __init__(self, queryInput):
        self.database = None
        self.tableName, self.targets, self.conditions = self.__parseUpdate(queryInput) 

    def execute(self):
        global db_runtime_context
        if db_runtime_context.current_db is None:
            print("!Failed to execute query because no database is selected!")
            return None 

        self.tableName = self.tableName.lower()
        
        if self.tableName is not None:
            if self.tableName in db_runtime_context.current_db.tables:
                pass
            else:
                print("!Failed to execute query on table", self.tableName, "because it does not exist!")
                return None 



            db_runtime_context.current_db.tables[self.tableName].update(self.targets, self.conditions)


    def __parseUpdate(self, queryInput):
        tableName = queryInput[0] 

        if queryInput[1].lower() != "set":
            print ("!Invalid SQL statement!")
            return None, None, None 
        

        joinStr = ' '.join(queryInput[2:]) 
        splitJoin = re.split("where", joinStr, flags=re.IGNORECASE)

        updates = {}
        conditions = None


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

        if len(splitJoin) > 1:
            conditions = list(filter(None, re.split(r"(=|!=|<>|<|>|<=|>=)", splitJoin[1])))
            conditions = [x.strip().replace("'", '') for x in conditions]
        
        return tableName, updates, conditions