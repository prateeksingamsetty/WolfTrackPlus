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
