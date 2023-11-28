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
