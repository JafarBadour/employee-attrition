# Importing module
import mysql.connector
import os
import time 

HOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASSWORD")

# Creating connection object
mydb = mysql.connector.connect(
        host = HOST,
        user = DBUSER,
        password = DBPASS
)
mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS InputTraffic;")
mydb.commit()
mydb.close()

def execute(sql_query):
    mydb = mysql.connector.connect(
        host = "attrdb.ceavtkczucln.eu-west-2.rds.amazonaws.com",
        user = "user",
        password = "123123123",
        db="InputTraffic"
    )
    
    cursor = mydb.cursor()
    cursor.execute(sql_query)
    print("ran command")
    mydb.commit()
    cursor.close()

    time.sleep(0.1)
    

# Printing the connection object

if __name__ == "__main__":


    sql_query = f"""
    CREATE TABLE IF NOT EXISTS Inputs (
    dt int,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"""
    execute(sql_query)
    while True:
        time.sleep(0.1)
        local_files = os.listdir(".")
        for f in local_files:
            if f.endswith(".csv"):

                import pandas as pd
                df = pd.read_csv(f)
                execute(f"INSERT INTO Inputs (dt ) VALUES ({len(df)} );")
                os.remove(f)
    

