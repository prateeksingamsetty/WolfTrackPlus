from datetime import datetime
from flask import Blueprint, flash, session
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user, login_manager
from werkzeug.utils import redirect
from Controller.user_controller import User
from Controller.application_controller import Application
from Controller.email_framework import *
import requests

api_key = '68188bd34eea4250107ae82ee6d61054'
app_id = '394232b1'
adzuna_api_url = 'https://api.adzuna.com/v1/api/jobs/us/search/1'
search_params = {
    'app_id': app_id,
    'app_key': api_key,
    'what': 'software engineer',  # Modify the search parameters
    'where': 'united states',      # Modify the location
    'content-type': 'application/json',
    'results_per_page': 40
}

home_route = Blueprint("home_route", __name__)

user = User()
application = Application()
# login = login_manager.LoginManager(application)


def fetch_upcoming_events_temp():
    response = requests.get(adzuna_api_url, params=search_params)
    upcoming_events_temp = []
    if response.status_code == 200:
        job_listings = response.json()
        for job in job_listings['results']:
            dic = {}
            dic["title"] = job['title']
            dic["company"] = job['company']['display_name']
            dic["location"] = job['location']['display_name']
            date = job['created']
            year, month, day = datetime.strptime(
                date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d").split('-')
            combined_date = f"{year}-{month}-{day}"
            dic["date_created"] = combined_date
            salary_max = job.get('salary_max', 'N/A')
            dic["salary"] = "$" + str(salary_max)
            dic['job_url'] = job['redirect_url']
            upcoming_events_temp.append(dic)
    return upcoming_events_temp


@home_route.route("/", methods=["GET"])
# def home():
#     return redirect("/auth")
@home_route.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", loginError="")


@home_route.route("/auth", methods=["GET"])
def auth():
    """
    redirects to home page after authentication, intercepts the get method.
    """
    if "email" in session:
        data = user.get_auth_user_dao(session["email"])
        data["wishlist"] = application.get(session["email"], "")
        response = requests.get(adzuna_api_url, params=search_params)
        upcoming_events = fetch_upcoming_events_temp()
        return render_template("home.html", data=data, upcoming_events=upcoming_events)
    else:
        return redirect("/login")


@home_route.route("/loginUser", methods=["GET", "POST"])
def loginUser():
    """
    When encoundering the /loginUser url, this is function is called. it intercepts both get and post requests.
    If recieved a get request, it fetches the login page. if recieved a post request, it checks if the login credentials are valid.
    If the credentials are valid then page is redirected home page of the user.
    """
    session["email"] = request.form["username"]
    password = request.form["password"]
    result = user.get(session["email"], password)
    error = ""
    if result == 0:
        error = "Email does not exits. Please enter a valid email."
        return render_template("login.html", loginError=error)
    elif result == 2:
        error = "Password incorrect."
        return render_template("login.html", loginError=error)
    else:
        return redirect("/auth")


@home_route.route("/signup", methods=["POST"])
def signup():
    """
    Intercepts the post request when hit with the /signup URL.
    This creates a new user for the application.
    This reads input from the form contents such as name email password gender location
    :return:
    """
    name = request.form["name"]
    session["email"] = request.form["email"]
    password = request.form["password"]
    print(name)
    gender = request.form["gender"]
    location = request.form["location"]
    result = user.post(name, session["email"], password, gender, location)
    if result == 0:
        error = "This email already exists. Please try with different email"
        return render_template("login.html", emailError=error)
    return redirect("/auth")


@home_route.route("/view", methods=["GET"])
# @login_required
def view():
    """
    This intercepts the /view URL get request. Displays the Page details for a application in a specific category.
    It reads the query parameters given when passing in the URL
    :return:
    """
    application_category = request.args.get("show").upper()

    result_data = application.get(session["email"], application_category)

    print(result_data)
    upcoming_events = fetch_upcoming_events_temp()
    return render_template(
        "view_list.html", data=result_data, upcoming_events=upcoming_events
    )


@home_route.route("/add_new_application", methods=["GET", "POST"])
# @login_required
def add_new_application():
    """
    This intercepts the add new application post request .
    It reads all the application details from the form contents during the post operation and creates a new application For the user .

    :return:
    """
    company_name = request.form["companyName"]
    location = request.form["location"]
    job_profile = request.form["jobProfile"]
    salary = request.form["salary"]
    username = request.form["username"]
    password = request.form["password"]
    security_question = request.form["securityQuestion"]
    security_answer = request.form["securityAnswer"]
    notes = request.form["notes"]
    date_applied = request.form["dateApplied"]
    status = request.form["status"]
    print("status", status)
    result = application.post(
        session["email"],
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
    )
    if result == 0:
        error = "This job application could not be stored in the database. Please try again."
        return render_template("home.html", jobAddError=error)
    data = {}
    s_email(
        company_name,
        location,
        job_profile,
        salary,
        # username,
        # password,
        session["email"],
        # security_question,
        # security_answer,
        # notes,
        # date_applied,
        status,
    )
    return redirect("/auth")


@home_route.route("/change_status_application", methods=["POST"])
# @login_required
def change_status_application():
    """
    It intercepts the change status application post request.
    It takes in the new status from the form content for the specific application ID and changes it to that status.
    :return:
    """
    status = request.form["status_change"]
    application_id = request.form["application_id"]
    print("status", status)
    result = application.change_status(application_id, status)
    if result == 0:
        error = "This job application could not be stored in the database. Please try again."
        return render_template("home.html", jobAddError=error)
    data = {}
    status_change_email(application_id, session["email"], status)
    return redirect("/auth")


@home_route.route("/delete_application", methods=["POST"])
# @login_required
def delete_application():
    """
    This intercepts the delete application post request it takes in the application ID and delete it from the database for the user
    :return:
    """
    application_id = request.form["application_id"]
    result = application.delete(application_id)
    if result == 0:
        error = "This job application could not be stored in the database. Please try again."
        return render_template("home.html", jobAddError=error)
    data = {}
    return redirect("/auth")


@home_route.route("/edit_application", methods=["POST"])
# @login_required
def edit_application():
    """
    This intercepts the edit application post request.
    It takes in the new details of the application for the given application ID and the user and modify the contents of the application in the database
    :return:
    """
    company_name = request.form["companyName"]
    location = request.form["location"]
    job_profile = request.form["jobProfile"]
    salary = request.form["salary"]
    username = request.form["username"]
    password = request.form["password"]
    security_question = request.form["securityQuestion"]
    security_answer = request.form["securityAnswer"]
    notes = request.form["notes"]
    date_applied = request.form["dateApplied"]
    status = request.form["status"]
    application_id = request.form["application_id"]
    print("status", status)
    result = application.update(
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
    )
    if result == 0:
        error = "This job application could not be stored in the database. Please try again."
        return render_template("home.html", jobAddError=error)
    data = {}
    return redirect("/auth")


@home_route.route("/edit_profile", methods=["POST"])
# @login_required
def edit_profile():
    """
    This intercepts the edit profile post request.
    It takes in the new profile details of the user and edits in the user database
    :return:
    """
    name = request.form["name"]
    gender = request.form["gender"]
    location = request.form["location"]
    user_id = request.form["user_id"]
    result = user.edit_profile(user_id, name, gender, location)
    if result == 0:
        error = "This user not found in the database. Please try again."
        return render_template("home.html", jobAddError=error)
    data = {}
    return redirect("/auth")


@home_route.route("/logout", methods=["GET"])
# @login_required
def logout():
    """
    Logs out the user when encountered with the logout URL get request and navigate back to the login URL
    :return:
    """

    if "email" in session:
        session.pop("email", None)
    # logout_user()
    return redirect("/login")


# if __name__ == '__main__':
#     app.run(debug=True)
