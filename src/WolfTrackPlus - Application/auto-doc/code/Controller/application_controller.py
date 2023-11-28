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


class Application:
    """
    This class is a controller for the application database. It inherits properties from flask_restful.Resource

    """


def __init__(self):
    """
    Default constructor that adds headers and application dao object on creation.
    """


def get(self, email, application_category):
    """
    Obtains stock information from the a url and adds a get request to controller
    :param email: email of the user
    :param application_category: the category of application
    @return: a string indicating the stock information and a string indicating cost of the product
    """


def post(
    self,
    email,
    company_name,
    location,
    job_profile,
    salary,
    username,
    password,
    security_question,
    security_answer,
    notes,
    date_applied,
    status,
):
    """
    Obtains stock information from the given url.

    :param url: URL of the product
    :return: a string indicating the stock information and a string indicating cost of the product
    """


def change_status(self, status, application_id):
    """
    Changes the state of a given application_id to given status
    """


def update(
    self,
    email,
    company_name,
    location,
    job_profile,
    salary,
    username,
    password,
    security_question,
    security_answer,
    notes,
    date_applied,
    status,
):
    """
    Updates any values changed in the profile and application parameters in website and database.
    """


def delete(self, application_id):
    """
    Deletes a given application from website and database.
    """
