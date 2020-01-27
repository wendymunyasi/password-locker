import pyperclip
import uuid

# Global Variables
global user_list


class User:
    """
    Class that generates new instances of the user
    """
    user_list = []  # Empty user list

    def __init__(self, first_name, last_name, number, email):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a user that matches that number.
        Args:
            number: Phone number to search for
        Returns :
            User that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls, number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls, number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


class Credentials:
    """
    Class that generates new instances of the credentials
    """
    credentials_list = []  # Empty user list

    @classmethod
    def user_exist(cls, first_name, number):
        '''
        Method that checks if a user exists from the user list.
        Args:
           first_name: Use this to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        current_user = ""
        for user in User.user_list:
            if (user.first_name == first_name and user.phone_number == number):
                current_user = user.first_name
        return current_user

    def __init__(self, first_name, last_name, app_name, email, phone_number, password, username):

        self.first_name = first_name
        self.last_name = last_name
        self.app_name = app_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.username = username

    @classmethod
    def find_by_number(cls, number):
        for credential in cls.credentials_list:
            if credential.phone_number == number:
                return credential

    @classmethod
    def find_by_username_and_app_name(cls, appname, username):
        for credential in cls.credentials_list:
            if (credential.app_name == appname and credential.username == username):
                return credential

    @classmethod
    def credential_exists(cls, number):
        for credential in cls.credentials_list:
            if credential.phone_number == number:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def display_all_credentials(cls):
        return cls.credentials_list

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        Credentials.credentials_list.remove(self)