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
    def find_by_number(cls,number):
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
