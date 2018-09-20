# match_file = open('/home/dell/PycharmProjects/data_project_unit_test/data/sample_matches.csv', 'r')
# read_file = open('/home/dell/PycharmProjects/data_project_unit_test/data/deliveries.csv', 'r')
# write_file = open('/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery.csv', 'r')
# list_of_list = []
# lst_id = []
# for line in csv.reader(match_file):
#     if line[0] not in lst_id:
#         lst_id.append(line[0])
# print(lst_id)
#
# for line in csv.reader(read_file):
#     if line[0] in lst_id:
#         list_of_list.append(line)
# print(len(list_of_list))
#
# writer = csv.writer(write_file)
# writer.writerows(list_of_list)

#
# dict_data = {}
# list_data = []
# for line in csv.reader(write_file):
#     if line[8] not in dict_data or line[0] not in dict_data:
#         dict_data[line[0]] = 0
#         dict_data[line[8]] = 0
#     if dict_data[line[8]] < 2:
#         list_data.append(line)
#         dict_data[line[8]] += 1
# print(list_data)
# read_file = open('/home/dell/PycharmProjects/data_project_unit_test/data/sample_delivery.csv', 'w')
# writer = csv.writer(read_file)
# writer.writerows(list_data)




# def check_database_existence(db_name):
#     sudo_password = 'admin@123'
#     command = 'sudo -u postgres psql template1 -U postgres -c SELECT 1 AS result FROM pg_database WHERE datname={};'\
#         .format(db_name)
#     command = command.split()
#
#     cmd1 = subprocess.Popen(['echo', sudo_password], stdout=subprocess.PIPE)
#     cmd2 = subprocess.Popen(['sudo', '-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
#     output = cmd2.stdout.read().decode()
#     print(output)
#
#     conn_obj = connect_db(database='postgres', user="postgres", password="postgres", host="localhost", port="5432")
#     cur = conn_obj.cursor()
#     print(cur.execute('''SELECT 1 AS result FROM pg_database WHERE datname={};'''.format(db_name)))
#
#     if output > 0:
#         print('This database already exist')
#         return True
#     else:
#         response = input('Do you want to create {db_name} as new database y/n')
#         if response == 'y' or response == 'Y':
#             print('Creating New Database {db_name}\n')
#             create_database(db_name)
#         else:
#             return False
