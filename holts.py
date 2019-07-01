# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:15:31 2019

@author: Ulfa
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='walet',
                             user='root',
                             password='')
   sql_select_Query = "select nilai from hargatotal_bw"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print (records)
   
   
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")