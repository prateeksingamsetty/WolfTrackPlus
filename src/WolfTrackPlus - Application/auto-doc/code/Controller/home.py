def login():
    """
    renders the html page for login, and takes user inputs .
    """


def auth():
    """
    Obtains the correct credentials, autheticates and creates a session for the user to stay logged in.

    """


def loginUser():
    """
    Obtains username, password to login to the user profile
    @return 0: If username does not exist, 2: Incorrect password, else: redirected to user page successfully.
    """


def signup():
    """
    This obtains all user information when user is signing up for the first time
    :param name:
    :param username:
    :param email:
    :param password:
    :param gender:
    :param location:

    @return 0: if email already exists, or network issue to create email profile, 1 : if profile is created successfully.
    """


def view():
    """
    Obtains the main page content of the wolftrackplus website.
    It contains the retrieval parameters to get custom events, deadlines, and incoming general deadlines.
    """


def add_new_application():
    """
        A new application is added with all the inputs user filled.
        .. list-table::
        :header-rows: 1

        * - Content
          - Value
        * - company Name
          - Name of the company
        * - Date Applied
          - Today's date
        * - Location
          - Location you entered for job application
        * - Salary
          - Your salary expectation
        * - User_name
          - Username you want to create in job application portal
        * - Password
          - Password you wish to set for the job application portal
        * - Security Question
          - Any relevant question you want to set
        * - Security Answer
          - Corresponding answer for the previous question
        * - Status
          - Applied
        * - Notes
          - Any notes or information you would like to share with the company

    |
    """


def change_status_application():
    """
    automatic update of any change in status of the application is updated here.
    @return 0: reports error and update will not be saved, 1: successful updation
    """


def delete_application(self, application_id):
    """
    deleted an application when delete button is clicked inside a particular application
    :param application_id: It is set internally when delete option on one application is clicked
    @return 0: if error, 1: if successfully deleted

    """


def edit_application():
    """
    edits contents related to job application and notifies user if edited successfully
    @return: 0 if error occurs, 1 if successfully edited and redirects to authentication page
    """


def edit_profile(self, request, user_id, name, gender, location):
    """
    From the request form created to change either user_id, name, gender, or location,
    One more paramters will be changed

    @return: 0 if error occurs, 1 if successfully changed
    """
    self.name = request.form["name"]
    self.gender = request.form["gender"]
    self.location = request.form["location"]
    self.user_id = request.form["user_id"]


def logout(self):
    """
    Logs out user when clicked logout button
    @return: login page of the website

    """
    self.session = None
