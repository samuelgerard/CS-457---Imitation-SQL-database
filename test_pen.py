import arguments as arg
import db_utility


string = '(a1 int, a2 varchar(20))'
string2 = ['(a1', 'int,', 'a2', 'varchar(20))']
string3 = 'CREATE TABLE tbl_1 (a1 int, a2 varchar(20))'
par = arg.arg_parser()

#par.establish_data_args(string)

print('b', par.establish_data_args(string3))

#db_utilit

