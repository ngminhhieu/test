import mysql.connector
import sshtunnel
import pandas as pd

def insert_varibles_into_table(name):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='AIOTlab2021',
            host='127.0.0.1',
            database='emed',
            port='3306')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO pill (name, created_by)
                            SELECT * FROM (SELECT %s, 25) AS tmp
                            WHERE NOT EXISTS (
                                SELECT name FROM pill WHERE name = %s
                            ) LIMIT 1; """
        record = (name, name)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into table Pill")

    except mysql.connector.Error as error:
        print("Failed to insert into table Pill {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


new_drugs = pd.read_csv('./new_drugs.csv')
for i in range(len(new_drugs)):
    insert_varibles_into_table(new_drugs.iloc[i,0])