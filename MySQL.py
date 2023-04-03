#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="Sraddha_1",user="sraddha",password="sraddha@99",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, topic, data
data={'Topic':'Humidity Sensor','Data':12.5}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO MQTT_1(Topic, Data)VALUES(%(Topic)s,%(Data)s);",data)
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

