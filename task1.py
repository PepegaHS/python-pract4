import csv
import json

# Преобразуйте данные из animals.csv в список словарей и сохраните результат
# в файл zoo.json.

animals_csv = [
    ['Животное','Среда обитания'],
    ['Медведь','Лес'],
    ['Верблюд','Пустыня']
]
animals_dict = {}
animals_json = []

with open('animals.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(animals_csv)

# with open('animals.csv', 'r',encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row_number, row in enumerate(reader, 1):
#         print("Строка",row_number, row)
#         print (f'Строка {type(row)}')

with open('animals.csv', 'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for i in reader:
        animals_dict[i['Животное']] = i['Среда обитания']
        animals_json.append(animals_dict)


print('---')
with open('zoo.json', 'w', encoding='utf-8') as file:
    json.dump(animals_json, file)

with open('zoo.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print('zoo.json: ',data)

