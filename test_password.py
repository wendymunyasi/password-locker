import unittest
import pyperclip
from password import User, Credentials


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

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "0712345678",
                         "test@user.com")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a contact object
        self.assertEqual(len(User.user_list), 1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "User", "0711223344",
                         "test@user.com")  # new user
        test_user.save_user()

        found_user = User.find_by_number("0711223344")

        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):
        '''
        test to check if a user actually exists and if we can return a boolean if it does not exist.
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "0711223344",
                         "test@user.com")  # new contact
        test_user.save_user()

        user_exists = User.user_exist("0711223344")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.user_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_user.save_user()
        User.copy_email("0707240068")

        self.assertEqual(self.new_user.email, pyperclip.paste())


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User(
            "Wendy", "Munyasi", "0707240068", "wendymunyasi@gmail.com.com")  # create contact object
        self.new_credential = Credentials(
            "Wendy", "Munyasi", "Twitter", "wendymunyasi@gmail.com", "0707240068", "nBD48gd6dD")

    def tearDown(self):
        '''
        tearDown method that does clean up aftereach test case has run.
        '''
        Credentials.credentials_list = []

    def test_user_exists(self):
        '''
        Test to check if a specific user exists.
        '''
        self.new_user.save_user()
        test_user = User("Wendy", "Munyasi", "0707240068",
                         "wendymunyasi@gmail.com")
        test_user.save_user()

        current_user = ""

        for user in User.user_list:
            if (user.first_name == test_user.first_name and user.phone_number == test_user.phone_number):
                current_user = user.first_name
                return current_user

        self.assertEqual(current_user, Credentials.user_exist(
            test_user.first_name, test_user.phone_number))

    def test_init(self):
        '''
        To test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "Wendy")
        self.assertEqual(self.new_credential.last_name, "Munyasi")
        self.assertEqual(self.new_credential.app_name, "Twitter")
        self.assertEqual(self.new_credential.email, "wendymunyasi@gmail.com")
        self.assertEqual(self.new_credential.phone_number, "0707240068")
        self.assertEqual(self.new_credential.password, "nBD48gd6dD")

    def test_save_credential(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("Wendy", "Munyasi", "Twitter", "wendymunyasi@gmail.com", "0707240068", "nBD48gd6dD")# new credential
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)


if __name__ == '__main__':
    unittest.main()
