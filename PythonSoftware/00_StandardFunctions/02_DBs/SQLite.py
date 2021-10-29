# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# SQLite examples
import sqlite3 as mdb
import os


def TableExists(DBName,TableName):
    #os.chdir("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/03_TrägheitTool/")
    # Checks if a table exists within a specific DB
    # Create a connection to the DB
    try:
        ConInfo=str("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/03_TrägheitTool/"+DBName+'.db')
        con = mdb.connect(ConInfo)
        # Create the cursor object
        cur = con.cursor()
    except Exception as ex:
        print('Connection to DB failed DBName:' + DBName)

    # Create the SQLite String to search for the table
    SQLiteCom=str('SELECT name FROM sqlite_master WHERE type='+"'table'" + " AND name='" + TableName + "'")
    # Must be: cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stocks'")
                 
    cur.execute(SQLiteCom)
    Table=cur.fetchall()

    if len(Table)!=0:  # If Table is not empty
        print('-----------------------------------------')
        print(TableName + ' Table exists')
        return True
    elif len(Table)==0:          # If Table is empty
        print('------------------------------------------')
        print(TableName + '! Table does not exist, first create table. For example:')
        print(" cur.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''') ")
                            #''CREATE TABLE Projekte3 (date text, trans text, symbol text, qty real, price real)'''

        return False


def DeleteSQLiteTable(TableName):
    print('Deletes SQLite table by name')


def CreateTableWithinDB(DBName, TableName, FieldsString):
    # Example: FieldsSting="date text, trans text, symbol text, qty real, price real"   hence Field_Name type(text or real), Field_Name type, Field_Name type
    exists=TableExists(DBName,TableName)
    # Create table only in the case it does not already exist
    if exists==False:
        ConInfo=str("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/03_TrägheitTool/"+DBName+'.db')
        con = mdb.connect(ConInfo)# Create the cursor object
        cur = con.cursor()
        # Create the SQLite command
        SQLCom=str("'''"+"CREATE TABLE """+ TableName +" (" + FieldsString + ")" +"'''")
        # Create the actual Table in the Database
        print(SQLCom)
        cur.execute(SQLCom)
        print('Table created')
        return True

def PrintTableList(DBName):
    
    # Checks if a table exists within a specific DB
    # Create a connection to the DB
    try:
        ConInfo=str("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/03_TrägheitTool/"+DBName+'.db')
        con = mdb.connect(ConInfo)
        # Create the cursor object
        cur = con.cursor()
    except Exception as ex:
        print('Connection to DB failed DBName:' + DBName)

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())

DBName='Projects'
TableName='Projekte8'
FieldsString='date text, trans text, symbol text, qty real, price real'
#FieldsString='Projekt text, Projektnummer real, Beschreibung text, Anzahl_Tools real'
# Check if table exists or create if not already existing
exists=TableExists(DBName,TableName)
# Create the table if it doesnt exist yet
#a=CreateTableWithinDB(DBName, TableName, FieldsString)
PrintTableList(DBName)

print('DB check END')






