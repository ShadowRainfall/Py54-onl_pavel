import getters
import validators
import json


def app():

    users = []
    file_path = str(validators.check_file())

    while True:
        operation = input('1. Authorisation\n2. Registration\n3. Show user data\n')
        operation = validators.except_unknown_operation(validators.exit_of_program(operation))

        if operation == 1:
            with open(file_path, 'r') as data_file:
                json.load(data_file)
            print('Input data')
            users_email = getters.get_mail(users, input('Your EMAIL: '))
            if not users_email:
                print('Bye-Bye')
                break
            else:
                users_password = getters.get_password(users, input('Your PASSWORD: '))
                if not users_password:
                    print('Bye-Bye')
                    break
                if validators.check_data(users, users_email, users_password):
                    print('AUTHORISATION IS SUCCESSFUL')
                    break
        elif operation == 2:
            reg_user = getters.registration()
            print("REGISTRATION DATA: ", reg_user)
            if reg_user:
                with open(file_path, 'r') as data_file:
                    data = json.load(data_file)
                user_exists = any(user['name'] == reg_user['name'] for user in users)
                if user_exists:
                    print('SUCH USER IS ALREADY EXISTS. PLEASE ENTER THE OTHER USERNAME')
                else:
                    users.append(reg_user)
                    with open(file_path, 'w') as data_file:
                        json.dump(users, data_file, indent=4)
                        data_file.close()
            else:
                print('REGISTRATION FAILED')
        elif operation == 3:
            with open(file_path, 'r') as filer:
                content = json.load(filer)
                print(content)
                filer.close()


app()
