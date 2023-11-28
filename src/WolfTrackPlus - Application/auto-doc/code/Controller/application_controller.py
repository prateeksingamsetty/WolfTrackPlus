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
