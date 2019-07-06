# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:50:47 2019

@author: Ulfa
"""

import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='walet',
                             user='root',
                             password='')
   sql_select_Query = "select * from hargatotal_bw"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in python_developers is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  developer record")
   for row in records:
       print("id = ", row[0], )
       print("volume = ", row[1])
       print("nilai  = ", row[2])
       print("id_bulan  = ", row[3])
       print("id_tahun  = ", row[4], "\n")
   cursor.close()
   
   
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")