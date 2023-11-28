from DAO.sql_helper import sql_helper


class user_dao:
    """
    Class that contains required functions for user_dao.
    """

    def __init__(self):
        """
        Default constructor for the user_dat class. Initializes self.__db with sql_helper()
        """

    def create_user(self, name, email, password, gender, location):
        """
        Creates a user based on the details provided.

        Args:
            name (string): Name of the user.
            email (string): email with which the user wishes to log in.
            password (string): Password to log in.
            gender (string): Gender of the user.
            location (string): Location where the user is currently present.

        Returns:
            bool: Executes the query to create a user and returns the execution status.
        """

    def get_user(self, email, password):
        """
        Fetches an existing user from the database.

        Args:
            email (string): email required for the user's login.
            password (string): Password for the user's login.

        Returns:
            bool: Executes the query to fetch a user and returns the execution status.
        """

    def get_auth_user(self, email):
        """
        Looks for the authenticated user into the WolfTrackPlus portal, and fetches their details.

        Args:
            email (string): Email identifier of the user.

        Returns:
            array[]: Returns an array/list of user details - full name, gender, location, user id.
        """

    def get_user_id(self, email):
        """
        Gets the user ID from given email.

        Args:
            email (string): email of the user whose ID you wish to fetch.
        """

    def update_details(self, user_id, name, gender, location):
        """
        Updates the details of an existing user.

        Args:
            user_id (string): New user ID to update.
            name (string): New name to update.
            gender (string): New gender to update.
            location (string): New location to update.

        Returns:
            bool: Executes the query to update a user and returns the execution status.
        """

    def delete_user(self):
        """
        Deletes the user.
        """
