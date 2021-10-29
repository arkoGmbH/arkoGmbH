# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# SQLite basic functions
import sqlite3 as mdb
import os


def TableExists(con,table_name):
    """
    Check if table allready exists
    :param: 
    :return:
    """
    cur = con.cursor()
    sql = str(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name=" + "'"+ str(table_name) + "'")
    cur.execute(sql)

    # Show if table exists or not
    if cur.fetchone()[0]==1 :
        exists=True
        print('Table exists.')
    else:
        exists=False
    
    return exists


def CheckCreateTable(con,table_name):
    """
    Create table if not existing (two functions in one)
    :param: 
    :return:
    """
    cur = con.cursor()
    sql = 'create table if not exists ' + table_name + ' (id integer, X real , Y real, type integer, units text)'
    cur.execute(sql)
    print(cur.fetchall())
    return


def PrintAllRows(con, table_name):
    """
    Query all rows in the MyTable table
    :param conn: the Connection object
    :return:
    """
    cur = con.cursor()
    b="SELECT * FROM 'XYProfil'"
    sql='SELECT * FROM '+"'"+ table_name+"'"

    #cur.execute("SELECT * FROM XYProfil")
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def DeleteSQLiteTable(con, TableName):
    """
    Delete a table by name within a DB established by connection con
    :param: 
    :return:
    """
    print('Deletes SQLite table by name')




def CreateTableWithinDB(con, TableName, FieldsStrings):
    """
    Create table within DBPathName with the FieldStings
    :param: 
    :return:
    """
    # Example: FieldsStings="date text, trans text, symbol text, qty real, price real"   hence Field_Name type(text or real), Field_Name type, Field_Name type
    exists=TableExists(con,TableName)
    # Create table only in the case it does not already exist
    if exists==False:
        cur = con.cursor()
        # Create the SQLite command
        SQLCom=str("'''"+"CREATE TABLE """+ TableName +" (" + FieldsStrings + ")" +"'''")
        # Create the actual Table in the Database
        print(SQLCom)
        cur.execute(SQLCom)
        print('Table created')
        return True

def PrintTableList(con):
    """
    Print all tables within a DB established with con
    :param: 
    :return:
    """
    # Checks if a table exists within a specific DB
    # Create a connection to the DB
    try:
        cur = con.cursor()
    except Exception as ex:
        print('Connection to DB failed, check connection definition')

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())



#----- OLD -------------------------------
def OLDTableExists(DBName,TableName):
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


def main():
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
