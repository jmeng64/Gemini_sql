
import sqlite3

## connection to SQLite


connection = sqlite3.connect("student2.db")

## create a cursor object to insert record, create table 

cursor = connection.cursor()

## create the bable 

table_info = """

create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), GRADE INT); 

"""

cursor.execute(table_info)


# insert some records 

cursor.execute( ''' insert into STUDENT VALUES('Krish', 'Data Science', 'A', 90) ''' )
cursor.execute( ''' insert into STUDENT VALUES('JM', 'Math', 'B', 85) ''' )
cursor.execute( ''' insert into STUDENT VALUES('John', 'Physics', 'C', 87 ) ''' )
cursor.execute( ''' insert into STUDENT VALUES('Kevin', 'Data Science', 'A', 95) ''' )
cursor.execute( ''' insert into STUDENT VALUES('Rob', 'Chemistry', 'E', 97 ) ''' )
cursor.execute( ''' insert into STUDENT VALUES('Amy', 'Prompt Engineering', 'F', 82) ''' )

connection.commit()

## displayt the records 

print("Here are the inserted records so far")

data=cursor.execute(''' select * from STUDENT ''' )
for row in data: 
    print(row )

connection.close() 

