from mysql import connector
from pathlib import Path
import sys
import csv


def connect_db(database, user, password, host):
    print("Connecting to the database")
    try:
        conn = connector.connect(database=database, user=user, passwd=password, host=host)
        # print("Opened Db successfully")
        return conn
    except connector.OperationalError as ex:
        print("Got an error while connecting to database", ex.args)
        return None
    except Exception as ex:
        print(ex.args)
        return None


def drop_table(db_name, table_name):
    conn_obj = connect_db(database=db_name, user="root", password="admin@123", host="localhost")
    cur = conn_obj.cursor()
    try:
        cur.execute('DROP TABLE {};'.format(table_name))
        cur.close()
    except Exception as ex:
        print(ex)


def create_table(file_url, db_name, table_name, first_col):
    create_query = 'CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, '.format(table_name)
    insert_query = 'INSERT INTO {} ('.format(table_name)
    lst_row_data = []

    with open(file_url, 'r') as file_handle:
        lst_fields = next(csv.reader(file_handle))
        for row in csv.reader(file_handle):
            if first_col == 'y' or first_col == 'Y':
                lst_row_data.append(tuple(row))
            else:
                lst_row_data.append(tuple(row[1:]))
        # print(lst_row_data)

    if first_col == 'y' or first_col == 'Y':
        first_col = 0
    else:
        first_col = 1

    for field in range(first_col, len(lst_fields)):
        create_query += "{} VARCHAR(255), ".format(lst_fields[field])
        insert_query += '{}, '.format(lst_fields[field])
    create_query = create_query.rstrip(', ') + ')'
    insert_query = insert_query.rstrip(', ') + ') VALUES ('

    for value_type in range(first_col, len(lst_fields)):
        insert_query += '%s, '
    insert_query = insert_query.rstrip(', ') + ')'
    # print(lst_fields)
    # print(create_query)
    # print(insert_query)
    create_database(db_name)
    conn_obj = connect_db(database=db_name, user="root", password="admin@123", host="localhost")
    cur = conn_obj.cursor()
    try:
        cur.execute(create_query)       # Creating table and the associated fields
        for row in lst_row_data:
            cur.execute(insert_query, row)     # Inserting all table data at once
        cur.execute('SHOW TABLES;')
        for i in cur:
            print(i)
        conn_obj.commit()
        conn_obj.close()
    except Exception as ex:
        print(ex)


def drop_database(db_name):
    conn_obj = connector.connect(user="root", password="admin@123", host="localhost")
    cur = conn_obj.cursor()
    try:
        cur.execute('DROP DATABASE {};'.format(db_name))
        cur.close()
    except Exception as ex:
        print(ex)


def create_database(db_name):
    conn_obj = connector.connect(user="root", password="admin@123", host="localhost")
    cur = conn_obj.cursor()
    try:
        cur.execute('CREATE DATABASE {};'.format(db_name))
        cur.close()
    except Exception as ex:
        print(ex)
        # sys.exit(ex)


def main():
    while True:
        print('Press 1 to CREATE a new Database')
        print('Press 2 to DROP a Database')
        print('Press 3 to CREATE a table in a given DATABASE from a CSV file')
        print('Press 4 to DROP a TABLE')
        print('Press 5 to Exit')
        selection_var = eval(input('Enter an integer for the choice given above\n'))
        if isinstance(selection_var, int) and selection_var in [1, 2, 3, 4, 5]:
            if selection_var == 1:
                database_name = input('Enter the name of the new Database\n')
                if database_name:
                    create_database(database_name)
                else:
                    print('Please specify a proper name for database')
            if selection_var == 2:
                database_name = input('Enter the name of the database to be Dropped\n')
                if database_name:
                    drop_database(database_name)
                else:
                    print('Please specify a name from existing Database list')
            if selection_var == 3:
                file_path = input('Enter the full path of the csv file for table creation\n')
                my_file = Path(file_path)
                if my_file.is_file():
                    database_name = input('Enter the name of the database in which you want to create table\n')
                    table_name = input('Enter the table name for the file\n')
                    first_column = input('Press y/Y to include first column of the csv file\n')
                    create_table(file_path, database_name, table_name, first_column)
                else:
                    print('File not found please try again!!!\n')
            if selection_var == 4:
                db_name, table_name = input("Enter the Database Name and Table Name respectively seperated by space\n").split()
                drop_table(db_name, table_name)
            if selection_var == 5:
                sys.exit('Thank You!!!')


if __name__ == '__main__':
    main()