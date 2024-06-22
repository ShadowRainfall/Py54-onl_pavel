import custom_exceptions
import calculating_functions


def user_data():
    while True:
        first_num = input('Your first number: ')
        first_num = custom_exceptions.except_only_number(custom_exceptions.exit_of_program(first_num))
        second_num = input('Your second number: ')
        second_num = custom_exceptions.except_only_number(custom_exceptions.exit_of_program(second_num))
        operation = input('Menu of operations:\n1 - addition\n2 - subtraction\n'
                          '3 - multiplication\n4 - division\n5 - exponentiation\n')
        operation = custom_exceptions.except_unknown_operation(custom_exceptions.except_only_number(operation))
        if operation == 1:
            print(f'Result of addition: [ {calculating_functions.addition(first_num, second_num)} ]')
        elif operation == 2:
            print(f'Result of subtraction: [ {calculating_functions.subtraction(first_num, second_num)} ]')
        elif operation == 3:
            print(f'Result of multiplication: [ {calculating_functions.multiplication(first_num, second_num)} ]')
        elif operation == 4:
            print(f'Result of division: [ {calculating_functions.division(first_num, second_num)} ]')
        elif operation == 5:
            print(f'Result of exponentiation: [ {calculating_functions.exponentiation(first_num, second_num)} ]')


user_data()
