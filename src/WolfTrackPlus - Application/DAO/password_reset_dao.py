from DAO.sql_helper import sql_helper


class password_reset_dao:
    """
    This is the application_dao class."
    """

    def __init__(self):
        """
        This is the default constructor for the application_dao class.
        """
        self.__db = sql_helper()


    def upsert_code(self, email, code):
        """
        Upserts password reset code based on email.

        Args:
            email (string): email of the user who created the application in respect.
            code (int): Application status such as pending or applied.

        Returns:
            [tuple]: Returns the result of the SQL query that fetches the application from the database.
        """

        sQuery = f"INSERT INTO password_reset(email, code) VALUES('{email}', {code}) ON DUPLICATE KEY UPDATE code = {code};"
        print(sQuery)

        res = self.__db.run_query(sQuery)

        return res

    def get_code(self, email):
        """
        Retrieves password reset code based on email.

        Args:
            email (string): email of the user who created the application in respect.

        Returns:
            [int]: Returns the result of the SQL query that fetches the application from the database.
        """

        result = self.__db.run_query(
            "SELECT code FROM password_reset WHERE email='"
            + email
            + "'"
        )
        print(result)
        if result is None:
            return None
        return result[0][0]

        sQuery = f"INSERT INTO password_reset(email, code) VALUES('{email}', {code}) ON DUPLICATE KEY UPDATE code = {code};"
        print(sQuery)

        res = self.__db.run_query(sQuery)

        return res


    def update_password(self, email, password):
        """
        Updates the password of a user based on email.

        Args:
            email (string): email with which the user wishes to log in.
            password (string): Password to log in.

        Returns:
            bool: Executes the query to create a user and returns the execution status.
        """
        return self.__db.run_query(
            "CALL UpdateUserPassword('"
            + email
            + "','"
            + password
            + "');"
        )
