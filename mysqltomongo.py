from pymongo import MongoClient
import mysql.connector
import pandas as pd
import numpy as np

""" This is a function that can be used to migrate MySQL data tables to MongoDB as Mongo Collections. Happy migrating! -Efe Büyük """


def transfer_table_mysql_to_mongo(mysqlDbName,mysqlTableName,mongoDbName,mongoTableName):

  # Mongodb Database
  cluster = MongoClient("#HERE YOU WILL USE YOUR USERNAME AND PASSWORD WITH YOUR LINK TO CONNECT MONGODB")
  mongodb = cluster[mongoDbName]
  collection = mongodb[mongoTableName]

  # MySQL Database
  mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=(mysqlDbName)
    )

  #Selecting the datas and columns from MySQL
  mycursor = mysqldb.cursor()
  mycursor.execute("SELECT * FROM {}".format(mysqlTableName))
  mysqldatas = mycursor.fetchall()
  mycursor.execute("SHOW COLUMNS FROM {}".format(mysqlTableName))
  columns = mycursor.fetchall()
  thecolumns = []
  for x in columns:
      thecolumns.append(x[0])

  #Transfering MySQL data to json like dict format in a list, using numpy and pandas
  dataArray = np.array(mysqldatas)
  dataFrame = pd.DataFrame(dataArray, columns=thecolumns)
  datas = dataFrame.to_dict(orient = 'records')

  #Importing the datas to MongoDB if they are not exist
  print("Migrating datas...")
  counter = 1
  for data in datas:
    collection.update_one(data,{'$setOnInsert':data},upsert = True)
    print("{} Data imported".format(counter))
    counter += 1

  print("All datas succesfully migrated")

#Using the function
"""On this example of migration from MySQL to Mongodb, i used 'testdatabase' as my database name and 'testtable'
as my table name."""

#transfer_table_mysql_to_mongo('testdatabase','testtable','testdatabase','testtable')

"""On this example of migration from MySQL to Mongodb, i used 'testdatabase' as my database name and 'testtable2'
as my table name."""

transfer_table_mysql_to_mongo('testdatabase','testtable2','testdatabase','testtable2')
