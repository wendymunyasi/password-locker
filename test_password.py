import unittest
from password import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User(
            "Wendy", "Munyasi", "0707240068", "wendymunyasi@gmail.com.com")  # create contact object

    def tearDown(self):
        '''
        tearDown method that does clean up aftereach test case has run.
        '''
        User.user_list = []

    def test_init(self):
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

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "0712345678",
                         "test@user.com")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()
