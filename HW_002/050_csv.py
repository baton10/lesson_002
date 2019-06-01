import csv

with open('expor.csv', 'w', encoding='utf-8', newline='\n') as f:
    fields = ['name', 'age', 'job']
    people = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

#    for a in lists:
#        print(list(a.keys()))