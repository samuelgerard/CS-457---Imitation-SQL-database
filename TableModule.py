import Joins

class Table(object):
    def __init__(self, dbName, tableName, newlyCreated=False):
        # Initialize member variables.
        self.dbName = dbName
        self.tableName = tableName
        self.fileName = tableName + ".tbl"
        self.safeName = tableName.lower()
        self.schema = {}
        self.rows = []
        

        # else:

    def print_name(self):
        print(self.tableName)
    
    def setSchema(self, schema):
            self.schema = schema

    def display_table_full(self):
        counter = 0
        max = len(self.schema)
        for key, value in self.schema.items():
            if counter == max - 1:
                print(key, value)
                break
            print(key, value, "| ", end = "")
            counter = counter + 1
        
        for dicts in self.rows:
            for k, v in dicts.items():
                print(v, end=" ")
            print('')
        
        print('\n')
        
    
    def addColumn(self, attributeName, dataType):
        '''
        Purpose:    Adds a column to the table.
        Parameters: attrName: column name to be added.
                    dataType: datatype of added column.
        Returns:    Returns True if column added.
        '''

        self.schema[attributeName] = dataType
        return True
    
    def insert(self, values, columns=None):
        '''
        Purpose : Insert some data to the table
    	Parameters :
    		values: A list of values to insert in the order of the table schema
            columns: A list of columns. If not included, length of values must be
                     the same as length of schema
    	Returns: Boolean corresponding to the status of the operation
        '''
        # For every attribute in the table, check if it exists in attrDataDict
        # If it does: Add the attrDataDict value to that spot, else add "NULL" there

        if columns is None:
            # Check that we have a value for every attribute
            if len(values) != len(self.schema):
                print("!Failed to insert on table", self.tableName,
                      "because there must be a value for every attribute")
                return False

            row = {}
            index = 0
            for attrName, dataType in list(self.schema.items()):
                # Check that the data type of this element is correct
                if not self.__isCastableTo(values[index], dataType):
                    print("!Failed to insert on table", self.tableName,
                          "because data type does not match schema!")
                    return False
                # Add to the row
                row[attrName] = values[index]
                index += 1
            self.rows.append(row)
            print("1 new record inserted.")
            return True

        else:
            if len(values) != len(columns):
                print("!Failed to insert on table", self.tableName,
                      "because there must be a value for every attribute")
                return False
            
            row = {}
            index = 0 
            for attrName, dataType in list(self.schema.items()):
                # Check to see if the column has data 
                if attrName in columns:
                    # Check the data type 
                    if not self.__isCastableTo(values[index], dataType):
                        print("!Failed to insert on table", self.tableName,
                              "because data type does not match schema!")
                        return False
                    # Add to the row 
                    row[attrName] = values[index]
                    index += 1
                else:
                    # Set value to NULL 
                    row[attrName] = "NULL"
            self.rows.append(row)
            print("1 new record inserted.")
            return True 
    
    def __isCastableTo(self, val, newType):
        '''
    	Purpose : Checks to see if a value is castable to a type
    	Parameters :
    		val: The value to try to cast
            newType: The type to attempt to cast val to
    	Returns: Boolean determining the result of the operation
        '''
        newType = self.getType(newType)
        if newType is str:
            return True
        try:
            self.castColumn(val, newType)
            return True
        except ValueError:
            return False
        
    def castColumn(self, column, castType):
        ''' 
        Purpose : Cast a value to a type
        Parameters : 
            column: The value to cast
            castType: The type to cast to
        Returns: The casted value
        ''' 
        return castType(column)

    def getType(self, string):
        ''' 
        Purpose : Get a python type from a string
        Parameters : 
            string: The string to parse
        Returns: A corresponding python type. None if no type matches
        ''' 
        string = string.split("(")
        string = string[0]
        string = string.lower()
        if string == "char":
            return str
        if string == "varchar":
            return str
        if string == "int":
            return int
        if string == "float":
            return float

    def update(self, updates, where=None):
        '''
        Purpose : Updates items from the table given certain conditions
    	Parameters :
            updates: A dictionary of updates to make to the table
    		where: A list of conditions. If None, update all entries in the table
    	Returns: Boolean representing status of the operation
        '''

        for column, value in list(updates.items()):
            if not self.attrExists(column):
                print("!Failed to update table", self.tableName,
                      "because", column, "is not an attribute in the table.")
                return False

        if where is None or len(where) == 0:
            for row in self.rows:
                for column, value in list(updates.items()):
                    row[column] = value
            return True


        column = where[0]
        operator = where[1]
        value = where[2]

        # Verify that the where column exists.
        if not self.attrExists(column):
            print("!Failed to update table", self.tableName, "because",
                  column, "is not an attribute in the table.")
            return False

        modified_records = 0
        
        #check against the conditional wherver in the table, update if successful find
        for row in self.rows:
            if self.conditionCheck(column, operator, value, row):
                for upCol, upVal in list(updates.items()):
                    row[upCol] = upVal
                modified_records = modified_records + 1

        if(modified_records == 1):
            print('1 record modified.')
        elif(modified_records > 1):
            print(modified_records, 'records modified.')

        return True
    
    def attrExists(self, attrName):
        ''' 
        Purpose : Determine if an attribute exists in the table schema
        Parameters : 
            attrName: The attribute name to search for 
        Returns: Boolean value corresponding to the result
        ''' 
        return self.__attrInSchema(attrName)
        
    def __attrInSchema(self, attrName):
        '''
    	Purpose:    Determines if a given column (by name) exists in the table.
    	Parameters: attrName: column name to search for.
    	Returns:    True if the column is in the table, False if not.
        '''
        return (attrName in self.schema.keys())
    
    def conditionCheck(self, column, operator, value, row):
        ''' 
        Purpose : Check if a set of values matches a conditional statement
        Parameters : 
            column: LHS of the conditional
            operator: operator as a string
            value: RHS of the conditional
            row: The row to compare with
        Returns: True if the values match the given conditional statement
        ''' 
        # Data sanitization
        column = column.strip().replace("'", '')
        operator = operator.strip()
        value = value.strip().replace("'", '')

        castType = None 
        try:
            castType = self.getType(self.schema[column])
            if '.' in value:
                castType2 = self.getType(self.schema[value])
                value = self.castColumn(row[value], castType2)
            else:
                value = self.castColumn(value, castType)
        except:
            return False 

        testValue = self.castColumn(row[column], castType)
        return self.__conditionCompare(testValue, operator, value)

    def __conditionCompare(self, lVal, operator, rVal):
        ''' 
        Purpose : Compare two values based on a string operator
        Parameters : 
            lVal: LHS
            operator: Operator as a string
            rVal: RHS
        Returns: The result of the comparison
        ''' 
        if operator == "=":
            return lVal == rVal
        if operator == "!=" or operator == "<>":
            return lVal != rVal
        if operator == "<":
            return lVal < rVal
        if operator == ">":
            return lVal > rVal
        if operator == "<=":
            return lVal <= rVal
        if operator == ">=":
            return lVal >= rVal
        return False

    def delete(self, where=None):
        '''
        Purpose : Delete items from the table given certain conditions
    	Parameters :
    		where: A list of conditions. If None, delete all entries in the table
    	Returns: Boolean representing status of the operation
        '''
        if where is None or len(where) == 0:
            self.rows = []
            return True

        # Check that the column exists
        column = where[0]

        if not self.attrExists(column):
            print("!Failed to delete from table", self.tableName,
                  "because column", column, "does not exist")
            return False

        delRows = self.getDataByAttrName('*', where)
        for row in delRows:
            self.rows.remove(row)
        print(len(delRows), "records" if len(
            delRows) > 1 else "record", "deleted.")
        return True
    
    def getDataByAttrName(self, attrList, where=None, joinType=None):
        '''
        Purpose:    Fetches table data from specified columns.
        Parameters: attrList: array of attributes to fetch.
                    where: conditional to filter (Not yet implemented)
        Returns:    array of tuples filtered by attributes requested.
        '''
        returnSet = []
        if ["*" in tmp for tmp in attrList][0]:
            attrList = list(self.schema.keys())
        if where is None or len(where) == 0:
            for row in self.rows:
                temp = {}
                for key in list(self.schema.keys()):
                    if key in attrList:
                        temp[key] = row[key]
                returnSet.append(temp)
        else:
            for row in self.rows:
                if self.conditionCheck(where[0], where[1], where[2], row):
                    temp = self.__buildRow(row, attrList)
                    returnSet.append(temp)
                elif joinType == Joins.LEFT_OUTER_JOIN:
                    # Set all values from left table to NULL 
                    prefix = self.__getPrefix(list(self.schema.keys())[0])
                    temp = self.__buildRow(row, attrList, joinType, prefix)
                    returnSet.append(temp)
            
        return returnSet

    def __buildRow(self, row, attrList, joinType=Joins.NO_JOIN, prefix=None):
        '''
    	Purpose : Build a row based on a join type
    	Parameters : 
            row: The row currently being looked at 
            attrList: The list of attributes to be returned 
    		joinType: the type of join performed
            prefix: The tablename used for building the row
    	Returns: A row built based on the join type / prefix given
        '''
        temp = {}
        for key in list(self.schema.keys()):
            if key in attrList:
                if joinType == Joins.LEFT_OUTER_JOIN and self.__getPrefix(key) != prefix:
                    temp[key] = ""
                else:
                    temp[key] = row[key]
        return temp
    
    def getFriendlyName(self):
        '''
        Purpose : Get the table name minus the extension
     	Parameters :
    		None
    	Returns: A string containing the friendly name of the table
        '''
        return self.safeName
    
    def printTableByAttr(self, attrList, where=None, joinType=None):
        ''' 
        Purpose : Print a table given attributes / conditionals
        Parameters : 
            attrList: A list of attributes to print
            where: Optional conditional
            joinType: Optional join type
        Returns: None
        ''' 
        header = ""
        body = ""
        rows = self.getDataByAttrName(attrList, where, joinType)
        index = 1
        if ["*" in tmp for tmp in attrList][0]:
            attrList = self.schema.keys()
        for attr in attrList:
            cleanAttr = attr.split(".")
            if( len(cleanAttr) > 1):
                cleanAttr = cleanAttr[1]
            else:
                cleanAttr = cleanAttr[0]
            header += cleanAttr + " " + self.schema[attr]
            header += "|" if(index<len(attrList)) else ""
            index += 1
        print(header)

        for row in rows:
            index = 1
            for value in row.values():
                body += value
                body += "|" if(index<len(row)) else ""
                index += 1
            body += "\n"
        body = body[0:-1]
        print(body)

