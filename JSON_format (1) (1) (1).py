# Задача №49. Создать телефонный справочник свозможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи. (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

import json
import pprint

phone_book = [
    {
    "name": "Ervin", 
    "surname": "Howell", 
    "phone": "1106926593"
    },
    {
    "name": "Clementine", 
    "surname": "Bauch", 
    "phone": "14631234447"
    },
    {
    "name": "Patricia", 
    "surname": "Lebsack", 
    "phone": ["4931709623", "4431709623"]
    }
]

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - show records | 2 - new_record | 3 - name search | q - Quit\n'


def load():
    with open(db_path, 'r', encoding='utf-8') as fh:
        phone_book_local = json.load(fh)
    print('Phone Data Base is loaded')
    return phone_book_local


def save():
    with open('phone_book.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
        print('Phone Data Base is saved')
# save()

# BDnew = load ()
# print(BDnew)


def print_book():
    with open(db_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    pprint.pprint(json_data)


def new_record():
    a = {}
    a["name"] = input('Put the name: '),
    a["surname"] = input('Put the surname: '),
    a["phone"] = list(input('Put a phone number: ').split())
    with open(db_path, encoding='utf8') as f:
        data = json.load(f)
        data.append(a)
        with open(db_path, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=1)


def name_search():
    with open('phone_book.json') as f:
        data = json.load(f)
    b = str(input("Enter the name: "))
    print(list(filter(lambda x:x["name"]==b, data)))


action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book()
    elif action == '2':
        new_record()
    elif action == '3':
        name_search()
    

