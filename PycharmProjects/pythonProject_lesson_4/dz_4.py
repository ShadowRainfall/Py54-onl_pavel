def check_data(email, password):
    for user in users:
        if email in user['email']:
            if password in user['password']:
                print(f'Welcom, dear {email}')
            return email
    else:
        print('Incorrect data. Please try again')
        return

def get_password(users):
    pwd = input('Your PASSWORD: ')
    for user in users:
        if pwd == user['password']:
            return pwd
    else:
        print('ERROR OF PASSWORD. TRY AGAIN')

def get_mail(users):
    email = input('Your EMAIL: ')
    if email == 'exit':
        print('EXITING...')
        return
    for user in users:
        if email == user['email']:
            print('User is here')
            return email
    else:
        print('ERROR OF EMAIL. TRY AGAIN')

def list_of_users_on_age(users, check_age):
    for user in users:
        if int(user['age']) >= int(check_age):
            print(user['name'], user['age'])

def citizenship_list(users):
    for user in users:
        if user['citizenship']:
            citizenship_dict = {user['name']: user['citizenship']}
            print(citizenship_dict)

def add_status(users):
    for user in users:
        if suspect(user):
            user['status'] = 'suspicious'
        elif non_suspect(user):
            user['status'] = 'not_suspicious'
    return users

def suspect(user):
    lasy = user['age'] > 18 and not user['is_working']
    young = user['age'] < 18 and user['is_working']
    return lasy or young

def non_suspect(user):
    lasy = user['age'] > 18 and user['is_working']
    young = user['age'] < 18 and not user['is_working']
    return lasy or young

users = [
    {
        'name': 'Victor',
        'age': 24,
        'is_working': False,
        'citizenship': ['Russian', 'England'],
        'email': 'vector@mail.ru',
        'password': 'vict1m'
    },
    {
        'name': 'Sasha',
        'age': 28,
        'is_working': True,
        'citizenship': ['Russian', 'Poland'],
        'email': 'alex@gmail.com',
        'password': 'aleksan2er'
    },
    {
        'name': 'Sergey',
        'age': 17,
        'is_working': False,
        'citizenship': ['Russian', 'German'],
        'email': 'sergio@rumbler.ru',
        'password': 'sergi0'
    },
    {
        'name': 'Vladislav',
        'age': 18,
        'is_working': False,
        'citizenship': ['Russian', 'France'],
        'email': 'slav@yandex.ru',
        'password': 'vla21slav'
    },
    {
        'name': 'Anton',
        'age': 17,
        'is_working': True,
        'citizenship': ['Russian', 'Italian'],
        'email': 'tosha@gmail.com',
        'password': 'an10on'
    }
]

print('[STATUS] ')
add_status(users)
check_data(get_mail(users), get_password(users))
check_age = input('Enter the age for cgecking: ')
list_of_users_on_age(users, check_age)