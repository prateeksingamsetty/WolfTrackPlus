from flask import make_response, Blueprint, request, jsonify, render_template
from flask_restful import Resource
from DAO.user_dao import user_dao
from flask_login import login_required

# add_user = Blueprint('add_user', )

# Specify the url end point for the function


class User(Resource):
    """
    This class is a controller for the user database. It inherits properties from flask_restful.Resource
    """

    def __init__(self):
        self.headers = {"Content-Type": "text/html"}
        self.user = user_dao()

    # @login_required
    def get(self, email, password):
        """
        gets defails of the specific user
        :param email: email of the user
        :param password: Password on user
        :return: returns the details of the user
        """
        return self.user.get_user(email, password)

    # @auth
    def get_auth_user_dao(self, email):
        """
        Checks if the user is passing the correct authentication request
        :param email: email of the user
        :return: checks if the user is authenticated
        """
        return self.user.get_auth_user(email)

    # @login_required
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
        return self.user.create_user(name, email, password, gender, location)

    # @login_required
    def put(self):
        """
        Modifies the user details
        :return: returns a modified user details
        """
        self.user.update_details()
        some_json = request.get_json()
        return {"you sent": some_json}, 200

    # @login_required
    def delete(self):
        """
        Delete the user From the database
        :return: returns the deleted user details from the database
        """
        self.user.delete_user()
        some_json = request.get_json()
        return {"you sent": some_json}, 200

    def edit_profile(self, user_id, name, gender, location):
        """
        Changing the user details in the database
        :param user_id: user ID of the user
        :param name: Modified name of the user
        :param gender: modified gender of the user
        :param location: modified location of the user
        :return: returns the new details of the user
        """
        return self.user.update_details(user_id, name, gender, location)
