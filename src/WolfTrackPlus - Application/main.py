from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api

# from Login.login import login_route
from Controller.application_controller import Application
from Controller.user_controller import User
from Controller.home import home_route

app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = "Sample"  # os.environ.get('SECRET_KEY')
api.add_resource(User, "/user")
api.add_resource(Application, "/application")
app.register_blueprint(home_route, name="login", url_prefix="/login")
app.register_blueprint(home_route, name="home", url_prefix="/")
app.register_blueprint(home_route, name="auth", url_prefix="/auth")
app.app_context().push()


if __name__ == "__main__":
    app.run(debug=True)
