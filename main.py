import dataBase_connection


def input_word(string):
    res = string.split(":")

    try:
        # con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\bhuts\PycharmProjects\MY_Dictionary\My_Dictionary.accdb;'
        # conn = pyodbc.connect(con_string)

        cursor = dataBase_connection.conn.cursor()

        cursor.execute('SELECT * FROM WORDS ORDER BY ID DESC')

        lst_fill_ind = cursor.fetchone()[0]
        nextid = lst_fill_ind + 1

        myuser = (nextid, res[0].capitalize(), res[1].capitalize())

        cursor.execute('INSERT INTO words VALUES (?,?,?)', myuser)
        dataBase_connection.conn.commit()
        print("Data Inserted")

    except dataBase_connection.pyodbc.Error as e:
        print("Error Occurred", e)

    except IndexError:
        print("The word is not in the database")


def find_word(string):
    res = string.split(":")
    try:
        # con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\bhuts\PycharmProjects\MY_Dictionary\My_Dictionary.accdb;'
        # conn = pyodbc.connect(con_string)

        cursor = dataBase_connection.conn.cursor()

        cursor.execute('SELECT * FROM words WHERE Word = ?', res[0].capitalize())

        result = cursor.fetchone()

        if result != None:
            if result[1] == res[0].capitalize():
                return True
            else:
                return False
        else:
            return False

    except dataBase_connection.pyodbc.Error as e:
        print("Error Occurred", e)


def display_meaning(string):
    res = string.split(":")
    try:
        # con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\bhuts\PycharmProjects\MY_Dictionary\My_Dictionary.accdb;'
        # conn = pyodbc.connect(con_string)

        cursor = dataBase_connection.conn.cursor()

        cursor.execute('SELECT * FROM words WHERE Word = ?', res[0].capitalize())

        for row in cursor.fetchall():
            print(row)

        dataBase_connection.conn.commit()

    except dataBase_connection.pyodbc.Error as e:
        print("Error Occurred", e)


def update_meaning(string):
    try:
        cursor = dataBase_connection.conn.cursor()

        updated_meaning = input(f"Enter the updated meaning of {string} : ")

        cursor.execute("UPDATE words SET Meaning = ? WHERE Word = ?", updated_meaning.capitalize(), string.capitalize())

        cursor.commit()
    except dataBase_connection.pyodbc.Error as e:
        print("Error Occurred", e)


if __name__ == "__main__":
    a = input("Want to enter any word please type Yes: ")
    a = a.capitalize()
    while a == "Yes":
        s = input("Enter: ")

        if find_word(s):
            display_meaning(s)
            b = input("Want to update the meaning(yes or no): ")
            b = b.capitalize()

            if b == "Yes":
                update_word(s)
            else:
                pass
        else:
            input_word(s)

