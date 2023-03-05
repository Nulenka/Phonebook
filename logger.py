from Phonebook.data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"What format do you prefer?\n\n"
                    f"1 var:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 var:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Enter the variant's number: "))

    while var != 1 and var != 2:
        print('Wrong number!')
        var = int(input("Enter the variant's number: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('1st file data:\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('2nd file data:\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


  
def put_data():
    print('What file data do yu want to change from?')
    data_first, data_second = print_data()
    number_file = int(input('Enter the file number: '))

    while number_file != 1 and number_file != 2:
        print('Wrong number!')
        number_file = int(input('Enter the file number: '))

    if number_file == 1:
        print("Which contact to change?")
        number_journal = int(input('Enter the contact number: '))
        number_journal -= 1
        
        print(f'Change the contact\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Changes are saved!')
    else:
        print("Which contact to change?")
        number_journal = int(input('Enter the contact number: '))
        number_journal -= 1
        
        print(f'Change the contact\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Changes are saved!')


def delete_data():
    print('What file data do yu want to delete from?')
    data_first, data_second = print_data()
    number_file = int(input('Enter the file number: '))

    while number_file != 1 and number_file != 2:
        print('Wrong number!')
        number_file = int(input('Enter the file number: '))

    if number_file == 1:
        print("Which contact do you want to delete?")
        number_journal = int(input('Enter the contact number: '))
        
        print(f'Delete the contact\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('The contact is deleted!')
    else:
        print("Which contact do you want to delete?")
        number_journal = int(input('Enter the contact number: '))
        
        print(f'Delete the contact\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('The contact is deleted!')
