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
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Wendy")
        self.assertEqual(self.new_user.last_name, "Munyasi")
        self.assertEqual(self.new_user.phone_number, "0707240068")
        self.assertEqual(self.new_user.email, "wendymunyasi@gmail.com.com")


if __name__ == '__main__':
    unittest.main()
