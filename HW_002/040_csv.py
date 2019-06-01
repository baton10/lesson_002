# import csv
#
# with open('expor.csv', 'w', encoding='utf-8', newline='\n') as f:

#     lists = [
#         {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
#         {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
#         {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#     ]
#

import csv

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()

    for user in user_list:
        writer.writerow(user)