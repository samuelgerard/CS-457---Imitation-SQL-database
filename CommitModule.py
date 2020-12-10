
from arguments import db_runtime_context

class commit_argument():

	def __init__(self):
		pass

	def execute(self):
		global db_runtime_context

		# Base Case, make sur
		if db_runtime_context.current_db is not None:
			db_runtime_context.current_db.tranasactionInProgress = False
			db_runtime_context.current_db.save()


			if db_runtime_context.current_db.successfulTransactions > 0:
				print("Transaction committed.")
			else:
				print("Transaction aborted.")
