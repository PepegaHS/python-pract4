import csv

test_csv = [
    ['Имя','Возраст','Город','Должность'],
    ['Андрей','21','Химки','Разработчик'],
    ['Николай','20','Москва', 'Дизайнер'],
    ['Максим','22','Москва', 'Менеджер']
]

with open('test_data_csv', 'w',encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_csv)

with open('test_data_csv', 'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for row_number, row in enumerate(reader, 1):
        print("Строка",row_number, row)

test_csv[0].append('Зарплата')
for i in range(len(test_csv)):
    if test_csv[i][3] == 'Разработчик':
        test_csv[i].append('120000')
    elif test_csv[i][3] == 'Менеджер':
        test_csv[i].append('100000')
    elif test_csv[i][3] == 'Дизайнер':
        test_csv[i].append('90000')

print('---')
for row in test_csv:
    print(row)

with open ('employees_with_salary.csv', 'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(test_csv)

