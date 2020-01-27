#!/usr/bin/env python3.6

from password import User, Credentials
import pyperclip


def create_user(fname, lname, phone, email):

    new_user = User(fname, lname, phone, email)
    return new_user


def save_users(user):

    user.save_user()


def del_user(user):

    user.delete_user()


def find_user(number):
    return User.find_by_number(number)


def check_existing_users(number):
    return User.user_exist(number)


def display_users():
    return User.display_users()


def create_credential(firstname, lastname, appname, emaill, phone_no, password, username):

    new_credential = Credentials(
        firstname, lastname, appname, emaill, phone_no, password, username)
    return new_credential


def save_credentials(credential):

    credential.save_credentials()


def del_credential(credential):

    credential.delete_credential()


def find_credential(number):
    return Credentials.find_by_number(number)


def check_existing_credentials(number):
    return Credentials.credential_exists(number)


def check_existing_credential_username_and_app_name(username, app_name):
    return Credentials.find_by_username_and_app_name(username, app_name)


def display_credentials():
    return Credentials.display_credentials()


def main():

    print("Hello Welcome to your user list. What is your name?")

    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these three short codes : cc - create a new user, dc - display user. fc - find user, ex - exit, del - delete user, co - copy user, cr - create a credential ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("First name ...")
            f_name = input().capitalize()

            print("Last name ...")
            l_name = input().capitalize()

            print("Phone number...")
            p_number = input()

            print("Email address ...")
            e_address = input().lower()

            save_users(create_user(f_name, l_name, p_number, e_address))
            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"Name: {user.first_name} {user.last_name}")
                    print(f"Phone: {user.phone_number}")
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any users saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()

            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "del":
            print("Are you sure you want to delete user? Input y or n")

            answer = input().lower()

            if answer == 'y':
                print("Enter the number of the user you want to delete")

                searched_number = input()

                if check_existing_users(searched_number):
                    searched_user = find_user(searched_number)
                    print(
                        f"{searched_user.first_name} {searched_user.last_name}")
                    print('-' * 20)

                    print(
                        f"Phone number.......{searched_user.phone_number}")
                    print(f"Email address.......{searched_user.email}")

                    print('\n')
                    print(" Is that the user you want to delete? Type y or n.")

                    answer_two = input()

                    if answer_two == 'y':
                        searched_user.delete_user()

                        print(f"User {f_name} {l_name} deleted")
                    else:
                        print('\n')

                else:
                    print("That user does not exist")

            else:
                print('\n')

        elif short_code == 'co':
            print("Enter the number of the user you want to copy")

            searched_number = input()

            if check_existing_users(searched_number):
                searched_user = find_user(searched_number)
                print(
                    f"{searched_user.first_name} {searched_user.last_name}")
                print('-' * 20)

                print(
                    f"Phone number.......{searched_user.phone_number}")
                print(f"Email address.......{searched_user.email}")

                print('\n')
                print(" Is that the user you want to copy? Type y or n.")

                answer_two = input()

                if answer_two == 'y':
                    pyperclip.copy(searched_user.phone_number)

                    print(
                        f"The copied user is: {searched_user.phone_number} ")
                    searched_user.phone_number, pyperclip.paste()

                else:
                    print('\n')

            else:
                print("That user does not exist")

        elif short_code == "cr":
            '''
            First check if the user exists
            '''
            print("Enter your phone number below to confirm if you exist. If you do, you will be redirected to a place to create your account.")

            search_number = input()

            if check_existing_users(search_number):

                search_user = find_user(search_number)
                print(f"Phone number ....{search_user.phone_number}")
                print(f"Email address...{search_user.email}")

                print('\n')
                print("Now let's create your credentials account")
                while True:
                    print("Use these short codes : cac - create a new credential account, dac - display a credential, fac - find a credential, ex - exit, dlt - delete a credential, ext - exit credential")

                    short_code = input().lower()

                    if short_code == 'cac':
                        print("New Credential")
                        print("-"*10)

                        print("First name...")
                        firstname = input().capitalize()

                        print("Last name")
                        lastname = input().capitalize()

                        print("App name")
                        app_name = input().capitalize()

                        print("Email")
                        emaill = input()

                        print("Phone Number")
                        phone_no = input()

                        print("Password")
                        password = input()

                        print("Username")
                        username = input()
                        print('\n')

                        save_credentials(create_credential(
                            firstname, lastname, app_name, emaill, phone_no, password, username))

                        print('\n')
                        print(
                            f"New Credential of the user {firstname} {lastname} created")
                        print('\n')

                    elif short_code == 'dac':

                        if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_credentials():
                                print(
                                    f"Name: {credential.first_name} {credential.last_name}")
                                print(f"App Name: {credential.app_name}")
                                print(f"Email: {credential.email}")
                                print(f"Phone No: {credential.phone_number}")
                                print(f"Password: {credential.password}")
                                print('\n')
                        else:
                            print('\n')
                            print("You don't seem to have any credentials saved yet")
                            print('\n')

                    elif short_code == 'fac':

                        print(
                            "Now, let's help you view your various credentials of various accounts")

                        print('\n')

                        print("Enter your phone number below")

                        search_number = input()

                        if check_existing_credentials(search_number):
                            search_credential = find_credential(search_number)
                            print(
                                f"{search_credential.first_name} {search_credential.last_name}")
                            print('-' * 20)

                            print(
                                f"Phone number: {search_credential.phone_number}")
                            print(f"App_name: {search_credential.app_name}")
                            print(f"Password: {search_credential.password}")
                        else:
                            print(
                                "The credentials belonging to {search_number} does not exist.")
                            print('\n')

                    elif short_code == 'dlt':

                        print("Are you sure you want to delete contact? Input y or n")

                        answer = input().lower()

                        if answer == 'y':
                            print(
                                "Enter the username and the app name of the credential you want to delete")

                            search_username = input()
                            search_app_name = input()

                            if check_existing_credential_username_and_app_name(search_username, search_app_name):

                                search_credential = Credentials.find_by_username_and_app_name(
                                    search_username, search_app_name)

                                print(
                                    f"{search_credential.first_name} {search_credential.last_name}")
                                print('-' * 20)

                                print(
                                    f"Username: {search_credential.username}")
                                print(
                                    f"App Name: {search_credential.app_name}")
                                print(
                                    f"Phone No: {search_credential.phone_number}")

                                print('\n')
                                print(
                                    "Is that the credential you want to delete? Type y or n")

                                answer_three = input().lower

                                if answer_three == 'y':
                                    search_credential.delete_credential()
                                else:
                                    print('\n')
                            else:
                                print("The credential does not exist")
                        else:
                            print('\n')

                    elif short_code == 'ext':
                        print("Thank you for using credentials app, Bye.....")
                        break

                    else:
                        print("I really didn't get that. Please use short codes")

            # elif:

            #     print("The user does not exist therefore you cannot make a credentials account with us")

        elif short_code == "ex":
            print("Bye .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
