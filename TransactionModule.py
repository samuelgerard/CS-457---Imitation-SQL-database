import os
import db_abstract 
from arguments import db_runtime_context


class begin_transaction:

	def __init__(self):
		pass

	def execute(self):
		global db_runtime_context

		if db_runtime_context is not None:
			print('Starting Transaction')
			db_runtime_context.current_db.transactionInProgress = True
			db_runtime_context.current_db.successfulTransctions = 0

			for tablename, table in list(db_runtime_context.current_db.tables.items()):
				if db_runtime_context.current_db.isWritable(table.tableName):
					self.createlockfile(table.tableName)

	def createlockfile(self, fName):
		pid = os.getpid()
		f = open(f"{db_runtime_context.current_db.db_name}/{fName}.{pid}", "w")
		f.close()