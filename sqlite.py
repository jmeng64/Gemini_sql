
import sqlite3

## connection to SQLite


connection = sqlite3.connect("student2.db")

## create a cursor object to insert record, create table 

cursor = connection.cursor()

## create the bable 

table_info = """

create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25)); 

"""

cursor.execute(table_info)


# insert some records 

cursor.execute( ''' insert into STUDENT VALUES('Krish', 'Data Science', 'A') ''' )
cursor.execute( ''' insert into STUDENT VALUES('JM', 'Math', 'B') ''' )
cursor.execute( ''' insert into STUDENT VALUES('John', 'Physics', 'C') ''' )
cursor.execute( ''' insert into STUDENT VALUES('Krish', 'Data Science', 'A') ''' )
cursor.execute( ''' insert into STUDENT VALUES('Rob', 'Chemistry', 'E') ''' )
cursor.execute( ''' insert into STUDENT VALUES('Amy', 'Prompt Engineering', 'F') ''' )

connection.commit()

## displayt the records 

print("Here are the inserted records so far")

data=cursor.execute(''' select * from STUDENT ''' )
for row in data: 
    print(row )

connection.close() 

