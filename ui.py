from Phonebook.logger import input_data, print_data, put_data, delete_data

def interface():
    print('Hello! What would you like to do?\n'
          '1. New record(2 formats)\n'
          '2. Delete contact\n'
          '3. Change data\n'
          '4. Print data\n')
    command = int(input("Enter the action number: "))

    while command < 1 or command > 4:
        print('Wrong number')
        command = int(input("Enter the action number: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()
