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


import unittest
from flask import Flask
from flask_testing import TestCase
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from your_flask_app import create_app, db


class TestFlaskApp(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        # Use in-memory database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['LOGIN_DISABLED'] = True  # Disable login for testing

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        response = self.client.get('/login')
        self.assert200(response)
        self.assert_template_used('login.html')

    def test_auth_redirect_without_session(self):
        response = self.client.get('/auth', follow_redirects=True)
        self.assertRedirects(response, '/login')

    def test_auth_with_session(self):
        with self.client:
            with self.client.session_transaction() as session:
                session['email'] = 'test@example.com'

            response = self.client.get('/auth')
            self.assert200(response)
            self.assert_template_used('home.html')

    # Add more test cases for other routes and functionalities


if __name__ == '__main__':
    unittest.main()
