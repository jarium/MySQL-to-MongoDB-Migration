# MySQL-to-MongoDB-Migration
With this function, you can migrate your MySQL data tables to your MongoDB data tables(collections)
The process is simple, just have your database and tables set up for both mysql and mongodb. Make sure you set your mongo connect and mysql connector inside the function and connect both servers correctly.
Once you done, just pass in your mysql db name, mysql table name and mongo db name, mongo table(collection) name to the function as parameters, then run the function.
If the data you are migrating does not exist in the mongodb collection, the function will migrate the data.
To make the function work, you need to have the following modules installed: pymongo, mysql.connector, pandas, numpy.

## Warning
This is just the script for simple migration actions. For multiworker version of this script, which will work as a docker container, please visit: https://github.com/jarium/MySQL-to-MongoDB-Migration-with-Celery-and-Docker
