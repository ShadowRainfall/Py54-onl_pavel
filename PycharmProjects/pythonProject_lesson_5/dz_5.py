import random


def compare(computer, three):
    i = 0
    count = 0
    for i in range(3):
        if three[i] in computer:
            print(f'Win number: {three[i]}')
            count += 1
        else:
            print(f'Wrong number: {three[i]}')
    if count == 3:
        print('You win')
    else:
        print('Try again')
        three = user_ask_three()
        compare(computer, three)


def user_ask_three():
    i = 0
    list_of_three = []
    while i in range(0, 3):
        user_number = input('Number: ')
        if str(user_number) == 'exit':
            print('Exiting...')
            return
        else:
            list_of_three.append(user_number)
            i += 1
    else:
        print('User three numbers: ', list_of_three)
        int_list_of_three = []
        for i in list_of_three:
            int_list_of_three.append(int(i))
        return int_list_of_three


def computer_ask_range(from_d, to_d):
    i = 0
    computer_range_list = []
    while i in range(0, 3):
        computer_range_number = random.randint(from_d, to_d)
        computer_range_list.append(int(computer_range_number))
        i += 1
    print('Computer_range: ', computer_range_list)
    return computer_range_list


def user_ask_range():
    user_range = []
    while True:
        count_of_numbers = input('Numbers count for range: ')
        start_number_of_range = input('Enter start number: ')
        last_number_of_range = input('Enter last number: ')
        if 'exit' in count_of_numbers and start_number_of_range and last_number_of_range:
            quit()
        try:
            int(count_of_numbers)
            int(start_number_of_range)
            int(last_number_of_range)
        except ValueError:
            print('Enter numbers only')
        else:
            break
    if 5 <= int(count_of_numbers) and 30 >= int(count_of_numbers):
        for i in range(0, int(count_of_numbers)):
            user_range.append(random.randint(int(start_number_of_range), int(last_number_of_range)))
        print('Enter three numbers')
        compare(computer_ask_range(int(start_number_of_range), int(last_number_of_range)), user_ask_three())
        print('ERROR OF RANGE')
    return


user_ask_range()
