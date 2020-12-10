
#this is a test run script that follows that exact PA_2 testing script
test_string_list_PA2 = ['create database CS457_PA2;', 'USE CS457_PA2;', 'Create table Product (pid int, name varchar(20), price float);',
            "insert into Product values(1, 'Gizmo', 19.99);", 
            "insert into Product values(2, 'PowerGizmo',     29.99);", 
            "insert into Product values(3, 'SingleTouch',    149.99);", 
            "insert into Product values(4, 'MultiTouch',     199.99);",
            "insert into Product values(5, 'SuperGizmo',     49.99);",
            "select * from Product;",
            "update Product set name = 'Gizmo' where name = 'SuperGizmo';",
            "update Product set price = 14.99 where name = 'Gizmo';",
            "select * from Product;",
            "delete from product where name = 'Gizmo';",
            "delete from product where price > 150;",
            "select * from Product;",
            "select name, price from product where pid != 2;"]

test_string_list_PA3 = ['create database CS457_PA3;',
                        'use CS457_PA3;',
                        'create table Employee (id int, name varchar(10));',
                        'create table Sales (employeeID int, productID int);'
                        "insert into Employee values(1,'Joe');",
                        "insert into Employee values(2,'Jack');",
                        "insert into Employee values(3,'Gill');",
                        "insert into Sales values(1,344);",
                        "insert into Sales values(1,355);",
                        "insert into Sales values(2,544);",
                        "select * from Employee E, Sales S where E.id = S.employeeID;",
                        "select * from Employee E inner join Sales S on E.id = S.employeeID;",
                        "select * from Employee E left outer join Sales S on E.id = S.employeeID;"]

test_string_list_PA4 = ['create database CS457_PA4;',
                        'use CS457_PA4;',
                        'create table Flights (seat int, status int);',
                        'insert into Flights values (22,0);',
                        'insert into Flights values (23,1);',
                        'begin transaction;',
                        'update flights set status = 1 where seat = 22;']
