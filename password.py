class User:
    """
    Class that generates new instances of the user
    """
    user_list = [] # Empty user list
    
    def __init__(self,first_name,last_name,number,email):
        
        """
        __init__ method that helps us define properties for our objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

