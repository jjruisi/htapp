import mysql.connector
from mysql.connector import Error

def dbinsert(array, location, lang):

    try:
        connection = mysql.connector.connect(host='htdbinstance.c95umtwikayo.us-east-2.rds.amazonaws.com',database='humantrafficking',user='humantrafficking',password='mr84CfyVWS7KP9E')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ",db_Info)
            cursor = connection.cursor()
            
            sql = "INSERT INTO TripAdvisor (url, review, location, lang) VALUE (%s, %s, %s, %s)"

            print(len(array))
            values = []
            for review in array:
                data = (review[0], review[1], location, lang)
                values.append(data)

            cursor.executemany(sql, values)
            connection.commit()
            print(cursor.rowcount, "records inserted")
            
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    except Error as e :
        print ("Error while connecting to MySQL", e)
