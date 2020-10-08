import db_abstract

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
        if self.current_db == database_name:
            print('That database is already being used!')
            return
        for set_db in self.database_archive: 
            if set_db.db_name == database_name:
                self.current_db = set_db
                print('the current database being used is now set to:', database_name)
                return
        print('That database does not exist')

    #display the current databases available and the current one being used
    def display_databases(self):
        if len(self.database_archive) != 0:
            for available in self.database_archive:
                print(available.db_name)
            print('The current database in use is:', self.current_db.db_name)
        else:
            print('Database archive is empty.')
    
    #delete a database
    def delete_database(self, database_name):
        for delete_db in self.database_archive:
            if delete_db.db_name == database_name:
                del delete_db
                print('Database ', database_name, ' successfully deleted')
        print('That database does not exit')

    #check if the current input_context is the same
    def same_input(self, check_same, database_name):
        for same in self.database_archive:
            if same.db_name == database_name:
                return True
        return False
