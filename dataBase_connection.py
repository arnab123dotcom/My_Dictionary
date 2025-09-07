import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\bhuts\PycharmProjects\MY_Dictionary\My_Dictionary.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected")

except pyodbc.Error as e:
    print("Error in Connection", e)