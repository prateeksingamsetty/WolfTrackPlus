class s_email:
    """
    A class that defines the email parameters.An email is sent when a new account is created, new job application is submitted, or a status change in application. It takes in the company_name, location, job_Profile, salary, username, password,email, security_question, security_answer, notes, date_applied, status, In this format, the email is sent from

    """


def status_change_email(application_id, email, status):
    """
    Send email for any change in status of application

    :param application_id: an ID is created when you sent a job application. That is used here.
    :param email: Your email ID mentioned in the job application will be notified.
    :param status: The status of your application change to "In Review", "Interview", "Offered", "Rejected", "No Longer under consideration"
    """
