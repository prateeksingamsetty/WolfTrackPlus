"""
MIT License

Copyright (c) 2023 Shiva Vara Prasad Kandhagatla, Prateek Singamsetty, Laasya Choudary Nandamuri, Jayanth Ramanidharan
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
