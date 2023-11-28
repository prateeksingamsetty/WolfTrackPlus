from DAO.sql_helper import sql_helper


class application_dao:
    """
    This is the application_dao class."
    """

    def __init__(self):
        """
        This is the default constructor for the application_dao class.
        """

    def add_application(
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
        Adds an application with all the specified arguments into the database.

        Args:
            email (string): Email ID of the user for that application.
            company_name (string): Company to which the user is applying to.
            location (string): Location of the job posting.
            job_profile (string): Type of role.
            salary (int): Salary that the job offers.
            username (string): Login credentials for the application.
            password (string): Password for the application.
            security_question (string): Security question for the application.
            security_answer (string): Answer to the application's security questions.
            notes (string): Any notes that the user might want to add in regards to their application.
            date_applied (date): Takes in the date of application.
            status (string): Status of this application such as applied or pending.

        Returns:
            self: runs the SQL query to add an application into the database, and returns the execution status of the query.
        """

    def get_application(self, email, application_status):
        """
        Fetches an application based on keywords from the database.

        Args:
            email (string): email of the user who created the application in respect.
            application_status (string): Application status such as pending or applied.

        Returns:
            [tuple]: Returns the result of the SQL query that fetches the application from the database.
        """

    def update_application(
        self,
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
        application_id,
    ):
        """
        Updates an application with all the specified arguments into the database.

        Args:
            email (string): Email ID of the user for that application.
            company_name (string): Company to which the user is applying to.
            location (string): Location of the job posting.
            job_profile (string): Type of role.
            salary (int): Salary that the job offers.
            username (string): Login credentials for the application.
            password (string): Password for the application.
            security_question (string): Security question for the application.
            security_answer (string): Answer to the application's security questions.
            notes (string): Any notes that the user might want to add in regards to their application.
            date_applied (date): Takes in the date of application.
            status (string): Status of this application such as applied or pending.

        Returns:
            self: runs the SQL query to update an application in the database, and returns the execution status of the query.
        """

    def change_status(self, application_id, status):
        """
        Changes the status of an existing application.

        Args:
            application_id (string): An identifier which can link to the required application.
            status (string): New status that the application should be changed into.

        Returns:
            bool: returns the status of the SQL query execution for changing application status.
        """

    def delete_application(self, application_id):
        """
        Deletes an existing application.

        Args:
            application_id (string): An identifier which can link to the required application.

        Returns:
            bool: returns the status of the SQL query execution for deleting an application.
        """
