import unittest
from password import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User(
            "Wendy", "Munyasi", "0707240068", "wendymunyasi@gmail.com.com")  # create contact object

    def test_instance(self):
        '''
        To test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Wendy")
        self.assertEqual(self.new_user.last_name, "Munyasi")
        self.assertEqual(self.new_user.phone_number, "0707240068")
        self.assertEqual(self.new_user.email, "wendymunyasi@gmail.com.com")

    def test_save_user(self):
        '''
        To test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
