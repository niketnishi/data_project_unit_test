### About 
This project imports match and delivery data from csv file and loads into the database and process the data 

#### Install and configure Mysql
```
$ sudo apt update
$ sudo apt install mysql-server
$ sudo mysql_secure_installation
```
Login to database for running queries on CLI
```
$ sudo mysqlq
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
Then, run ```FLUSH PRIVILEGES``` which tells the server to reload the grant tables and put your new changes into effect:
```
mysql> FLUSH PRIVILEGES;
```
Run mysql with user as root which will prompt for password which you have set previously.
```
$ mysql -u root -p
```

#### Stop Mysql server
```
sudo systemctl start mysql
```
#### Stop Mysql server
```
sudo /etc/init.d/mysql stop
```

#### Some Database queries
```
USE <DatabaseName>;
```
```
SHOW DATABASES;
```
```
CREATE DATABASE <DatabaseName>;
```
```
DROP DATABASE <DatabaseName>;
```
```
SHOW TABLES;
```
```
CREATE TABLE <TableName>;
```
```
DROP TABLE <TableName>;
```


#### Create Database table by choosing from the options below

```python
/usr/bin/python3.6 /home/dell/PycharmProjects/data_project_unit_test/src/read_csv_create_table.py
Press 1 to CREATE a new Database
Press 2 to DROP a Database
Press 3 to CREATE a table in a given DATABASE from a CSV file
Press 4 to DROP a TABLE
Press 5 to Exit
Enter an integer for the choice given above
``` 
#### Using Mysql connector to connect to database

```python
from mysql import connector
```

## Some Useful Links
```python
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04
```