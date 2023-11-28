class FlaskTest:
    """
    It is the subject body to write all unit testcases for login page
    """


def test_index(self):
    """
    test checks if login page is successfully
    @return: status code 308 if successfull
    """


def test_index_content(self):
    """
    test checks if login page is returning html/json file while executing and authenticating login
    """


def test_valid_email(self):
    """
    test checks if the email used for login already exists.
    It also checks the username and password are entered correctly during login
    @return: 200 if email is within database and password is correct
    """


def test_validate_credentials(self):
    """
    test checks if the username and password used for login are entered correctly during login
    @return: 200 if username and password are correct.
    """


def test_repeated_signup(self):
    """
    tests whether duplicate sign up of the same email id is avoided.
    @return: 400 and no duplicate will be created
    """


def test_new_application(self):
    """
    test checks if a new application is created correctly with entered information
    @param appplication_features: email, company_name,location, job_profile,salary,username,password,security_question,security_answer,notes,date_applied,status,):
    @return: 400 if successfully created a new application
    """


def test_edit_application(self):
    """
    it verifies valid credentials for the application being edited, then creates session
    The application paramrters will be updates to the respective application_id within database and website
    @return: 400 if successfully updated an existing application
    """


def test_edit_profile(self):
    """
    test checks if any modification to profile information is updated successfully.
    @return: 400 if successfully updated an existing user profile
    """
