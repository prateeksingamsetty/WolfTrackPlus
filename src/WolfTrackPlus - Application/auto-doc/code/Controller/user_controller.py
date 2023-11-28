class User:
    """
    This class is a controller for the user database. It inherits properties from flask_restful.Resource
    """

    def get(self, email, password):
        """
        gets defails of the specific user
        :param email: email of the user
        :param password: Password on user
        :return: returns the details of the user
        """

    def get_auth_user_dao(self, email):
        """
        Checks if the user is passing the correct authentication request
        :param email: email of the user
        :return: checks if the user is authenticated
        """

    def post(self, name, email, password, gender, location):
        """
        Create a new user with the given details
        :param name: name of the user
        :param email: email or the user
        :param password: password of the user
        :param gender: gender of the user it can be male or female
        :param location: location string of the user
        :return: returns the new user object that is created
        """

    def put(self):
        """
        Modifies the user details
        :return: returns a modified user details
        """

    def delete(self):
        """
        Delete the user From the database
        :return: returns the deleted user details from the database
        """

    def edit_profile(self, user_id, name, gender, location):
        """
        Changing the user details in the database
        :param user_id: user ID of the user
        :param name: Modified name of the user
        :param gender: modified gender of the user
        :param location: modified location of the user
        :return: returns the new details of the user
        """
