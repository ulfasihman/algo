# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:08:17 2019

@author: Ulfa
"""
import numpy as np
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='', db='walet')
curs = conn.cursor() #Use a client side cursor so you can access curs.rowcount
numrows = curs.execute("SELECT volume,nilai FROM hargatotal_bw")

#curs.fecthall() is the iterator as per Kieth's answer
#count=numrows means advance allocation
#dtype='i4,i4' means two columns, both 4 byte (32 bit) integers
A = np.array(curs.fetchall())

print (A) #output entire array