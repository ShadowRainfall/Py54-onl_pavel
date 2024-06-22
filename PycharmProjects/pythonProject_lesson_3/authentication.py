# def check_pwd(pwd, file):
#     file = open("/home/userd/PycharmProjects/pythonProject_lesson_3/password.txt", "rt")
#     read = file.readline()
#     print("File content:", read)
#     if str(pwd) == str(read):
#         print('WELCOME')
#     else:
#         print('WRONG PASSWORD')
#         file.close()
#     return None
#
# def get_pwd(pwd, file):
#     print('Enter password')
#     pwd = input()
#     check_pwd(pwd, file)
#     return pwd
#
# def check_name(name):
#     i = 0
#     if len(name) < 2:
#         print('Error. The name is too short. The name must contain more then 1 character')
#         return None
#     elif len(name) > 10:
#         print('Error. The name is too long. The name must contain less then 11 characters')
#         return None
#     if name in name_tuple:
#         return name
#     else:
#         i += 1
#         print(f'Name [ {name} ] not found. Try again!')
#     return None
#
# def get_name():
#     print('Enter Username')
#     g_name = input()
#     # check_name(g_name)
#     return g_name
#
# ar, s, ak, m, v = ('Artyom', 'Akim', 'Maksim', 'Sergey', 'Vladislav')
# name_tuple = (ar, s, ak, m, v)
# pwd = 0
#
# while True:
#     name = get_name()
#     if not name == "exit":
#         print('checking the name...')
#         if not check_name(name) == None:
#             print(f'Hello [ {name} ]')
#             file = open("/home/userd/PycharmProjects/pythonProject_lesson_3/password.txt", "r+")
#             get_pwd(pwd, file)
#             break
#         else:
#             print("ERROR")
#     else:
#         print('EXIT OF THE PROGRAM')
#         break

# users = [('u1', 'p1'), ('u2', 'p2'), ('u3', 'p3')]
#
# def check_pwd(pwd):
#     if len(pwd) < 2:
#         print('Error. The password is too short. The password must contain more then 1 character')
#         return None
#     elif len(pwd) > 10:
#         print('Error. The password is too long. The password must contain less then 11 characters')
#         return None
#     else:
#         return pwd
#
#     return check_pwd(pwd)
#
# def get_pwd():
#     pwd = input('Enter password')
#     return pwd
#
# def check_name(name):
#     i = 0
#     if len(name) < 2:
#         print('Error. The name is too short. The name must contain more then 1 character')
#         return None
#     elif len(name) > 10:
#         print('Error. The name is too long. The name must contain less then 11 characters')
#         return None
#
#     return None
#
# def get_name():
#     name = input('Enter Username')
#     return name
#
# while True:
#     name = get_name()
#     name_check = check_name(name)
#     pwd_check = check_pwd(get_pwd())
#     if name_check and pwd_check:
#         print(f'HELLO {name}')
#         break
#     print('Authentication error. Check name or password')

def check_password(password):
    if len(password) < 2:
        print('Error. The password is too short. The password must contain more then 1 character')
        return None
    elif len(password) > 10:
        print('Error. The password is too long. The password must contain less then 11 characters')
        return None
    return password

def get_password():
    password = input('Enter password\n')
    return password

def check_name(name):
    if len(name) < 2:
        print('Error. The name is too short. The name must contain more then 1 character')
        return None
    elif len(name) > 10:
        print('Error. The name is too long. The name must contain less then 11 characters')
        return None
    return name

def get_name():
    name = input('Enter Username\n')
    if name == 'exit':
        print('closing the application')
        exit()
    return name

name = get_name()
password = get_password()
name_checked = check_name(name)
password_checked = check_password(password)
while True:
    if name_checked and password_checked:
        print(f'HELLO [ {name} ]')
        break
