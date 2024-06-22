import os


class UnknownOperation(Exception):
    def __str__(self):
        return 'EXCEPTION: Unknown operation. Please, enter the right operation'


class OnlyNumbersEx(ValueError):
    def __str__(self):
        return 'EXCEPTION: You should use only numbers'


def check_data(users, email, password):
    for user in users:
        if email == user['email'] and password == user['password']:
            print(f'Welcome, dear [ {email} ]')
            return True
    print('Incorrect data. Please try again')
    return False


def exit_of_program(inp):
    if inp == 'exit':
        quit()
    else:
        return int(inp)


def except_only_number(num):
    try:
        if not num.isdigit():
            raise OnlyNumbersEx
        else:
            return int(num)
    except OnlyNumbersEx as g:
        print(g)


def except_unknown_operation(operation):
    try:
        list_num = [1, 2, 3]
        if operation in list_num:
            return operation
        else:
            raise UnknownOperation
    except UnknownOperation as e:
        print(e)
        return None


def check_file():
    path = '/home/PycharmProjects/pythonProject_lesson_6/data.json'
    try:
        if os.path.exists(path):
            return path
        else:
            print('DATA FILE IS LOST. CREATING OF NEW DATA FILE')
            with open(path, 'w') as file:
                file.write('[]')
            return path
    except Exception as e:
        print(e)
        return None
