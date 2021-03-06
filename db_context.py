import db_abstract
import os

class db_context:
    """
    Holds the current available database instances along with the other available databases at hand to use
    """

    def __init__(self, passed_db = None, database_archive = []):
        self.current_db = passed_db #the current database in use
        self.database_archive = database_archive # the list of references to database objects
    
    #input is a database object
    def add_database_to_archive(self, input):
        self.database_archive.append(input)

    #set the current database being used
    def set_database(self, database_name):
        if database_name in next(os.walk("."))[1]:
            if self.current_db is not None:
                self.current_db.save()
            self.current_db = db_abstract._db_abstract_(database_name)
            print('Now using Database: ', database_name)
        # for set_db in self.database_archive: 
        #     if set_db.db_name == database_name:
        #         self.current_db = set_db
        #         print('the current database being used is now set to:', database_name)
        #         return
        else:
            print('That database does not exist')

    #display the current databases available and the current one being used
    def display_databases(self):
        if len(self.database_archive) != 0:
            for available in self.database_archive:
                print(available.db_name)
            print('The current database in use is:', self.current_db.db_name)
        else:
            print('Database archive is empty.')
    
    def display_table(self, name):
        if name in self.current_db.tables:
            self.current_db.tables[name].display_table_full()
        else:
            print('That table does not exist!')
    
    def display_all_tables(self):
        for everything in self.current_db.tables:
            print(everything)

    def empty(self):
        if self.current_db is None:
            return True
        return False

    
    #delete a database
    def delete_database(self, database_name):
        for i, v in enumerate(self.database_archive):
            if v.db_name == database_name:
                del self.database_archive[i]
                print('Database', database_name, 'successfully dropped')
                return
        print('That database does not exist! cannot initiate a drop.')
    
    def delete_table(self, table_name):
        print(table_name)
        if table_name in self.current_db.tables:
            del self.current_db.tables[table_name]
            print('Table', table_name, 'successfully dropped' )
        else:
            print('Invalid table name! cannot initiate a drop')

    #check if the current input_context is the same
    def same_input(self, check_same, database_name):
        for same in self.database_archive:
            if same.db_name == database_name:
                return True
        return False

    def save(self):
        for save_db in self.database_archive:
            save_db.save()
