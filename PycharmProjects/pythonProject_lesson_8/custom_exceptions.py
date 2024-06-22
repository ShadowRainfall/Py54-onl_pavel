class UnknownOperation(Exception):
    def __str__(self):
        return 'EXCEPTION: Unknown operation. Please, enter the right operation'


class OnlyNumbersEx(ValueError):
    def __str__(self):
        return 'EXCEPTION: You should use only numbers'


class ExitProgram(SystemExit):
    def __str__(self):
        return 'EXCEPTION: EXIT ERROR'


def exit_of_program(inp):
    if inp == 'exit':
        quit()
    else:
        return inp


def except_only_number(num):
    try:
        if not num.isdigit():
            raise OnlyNumbersEx
        else:
            return int(num)
    except OnlyNumbersEx as g:
        print(g)


def except_devision(first, second):
    try:
        first / second
    except ZeroDivisionError:
        print('EXCEPTION: Dividing by 0 is a mistake')


def except_unknown_operation(operation):
    try:
        list_num = [1, 2, 3, 4, 5]
        if operation in list_num:
            return operation
        else:
            raise UnknownOperation
    except UnknownOperation as e:
        print(e)
