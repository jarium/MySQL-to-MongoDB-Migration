# MySQL-to-MongoDB-Migration
With this function, you can migrate your MySQL data tables to your MongoDB data tables(collections)
The process is simple, just have your database and tables set up for both mysql and mongodb. Make sure you set your mongo connect and mysql connector inside the function and connect both servers correctly.
Once you done, just pass in your mysql db name, mysql table name and mongo db name, mongo table(collection) name to the function as parameters, then run the function.
If the data you are migrating does not exist in the mongodb collection, the function will migrate the data.
