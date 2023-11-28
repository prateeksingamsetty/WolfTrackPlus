import pymysql
import os


class sql_helper:
    """
    This class contains the necessary supporting funtions to perform SQL related operations.
    """

    def __init__(self):
        """
        Default constructor for class sql_helper
        """

    def connect_database(self):
        """
        This function connects to the database on AWS, and authenticates the user.
        """

    def disconnect_database(self):
        """
        This function closes the database connection once done with it.
        """

    def run_query(self, query):
        """
        Runs the specified query through the database and returns the output.

        Args:
            query (string): [Requires a valid SQL query passed as an argument.]

        Returns:
            [Tuple(Tuple..)]: [The output of the query being executed on the database is returned in the form of nested tuples.]
        """
