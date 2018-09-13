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