import json
import validators


def registration():
    name = input('Input Username: ')
    email = input('Input email: ')
    pwd = input('Input password: ')
    pwd_trust = input('Input password for trusting: ')

    if pwd == pwd_trust:
        return {
            "name": name,
            "email": email,
            "password": pwd
        }
    else:
        print('WRONG TRUST PASSWORD')
        return None


def get_mail(users, email):
    for user in users:
        if email == user['email']:
            print('User is here')
            return email
    else:
        print('ERROR OF EMAIL. TRY AGAIN')
        return None


def get_password(users, pwd):
    for user in users:
        if pwd == user['password']:
            return pwd
    else:
        print('ERROR OF PASSWORD. TRY AGAIN')
        return None
