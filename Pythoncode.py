import pyodbc
import os
import sys
conn = pyodbc.connect('DSN=MSConnect; Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("CREATE TABLE DataAll(Customer VARCHAR(50),ProductCategory VARCHAR(50),PromoGroup VARCHAR(50),Datetime VARCHAR(50),Cases REAL,DemandAll REAL,RSV REAL,GSV REAL,Contribution REAL,NSV REAL,SVC REAL, ListPrice REAL)")
conn.commit()
conn.close()