from flask import make_response, Blueprint, request, jsonify, render_template
from flask_restful import Resource
from DAO.password_reset_dao import password_reset_dao
from flask_login import login_required

# add_user = Blueprint('add_user', )

# Specify the url end point for the function


class PasswordReset(Resource):
    """
    This class is a controller for the user database. It inherits properties from flask_restful.Resource
    """

    def __init__(self):
        self.headers = {"Content-Type": "text/html"}
        self.password_reset = password_reset_dao()

    # @login_required
    def upsert(self, email, code):
        """
        upserts reset code of the specific user
        :param email: email of the user
        :param code: reset code
        :return: returns the details of the user
        """
        return self.password_reset.upsert_code(email, code)

    def get_code(self, email):
        """
        retrieves reset code of the specific user
        :param email: email of the user
        :return: returns the reset code of the user
        """
        return self.password_reset.get_code(email)

    def update_password(self, email, password):
        return self.password_reset.update_password(email, password)