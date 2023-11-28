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


from main import app
from unittest.main import main
from flask import app
from flask.typing import StatusCode
import unittest
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class FlaskTest(unittest.TestCase):

    # check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if content returned is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # check data returned
    def test_valid_email(self):
        tester = app.test_client(self)
        response = tester.post(
            "/loginUser", data={"username": "wrongformat.com", "password": "password"}
        )
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_validate_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            "/loginUser", data={"username": "test@gmail.com", "password": "pasword"}
        )
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_validate_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            "/loginUser", data={"username": "test@gmail.com", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)

    def test_repeated_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            "/signup",
            data={
                "username": "test@gmail.com",
                "password": "password",
                "name": "test",
                "gender": "Female",
                "location": "Raleigh",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_new_application(self):
        with app.test_client(self) as c:
            with c.session_transaction() as sess:
                sess["email"] = "test@gmail.com"
                sess["password"] = "password"
        response = c.post(
            "/add_new_application",
            data={
                "companyName": "ANB",
                "location": "Seattle",
                "jobProfile": "Software Engineer",
                "salary": 80000,
                "securityQuestion": "What is the name of your first dog?",
                "securityAnswer": "Tommy",
                "dateApplied": "2021-02-01",
                "notes": "Check back in 2 weeks",
                "username": "abc@adobe.com",
                "password": "password1",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_edit_application(self):
        with app.test_client(self) as c:
            with c.session_transaction() as sess:
                sess["email"] = "swetha1189@gmail.com"
                sess["password"] = "thanks123"
        response = c.post(
            "/edit_application",
            data={
                "companyName": "ANB",
                "location": "Seattle",
                "jobProfile": "Software Engineer",
                "salary": 80000,
                "securityQuestion": "What is the name of your first dog?",
                "securityAnswer": "Tommy",
                "dateApplied": "2021-02-01",
                "notes": "Check back in 2 weeks",
                "username": "abc@adobe.com",
                "password": "password1",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_edit_profile(self):
        with app.test_client(self) as c:
            with c.session_transaction() as sess:
                sess["email"] = "shivakandhagatla1999@gmail.com"
                sess["password"] = "12345"
        response = c.post(
            "/edit_profile", data={"name": "sravya", "location": "Seattle"}
        )
        self.assertEqual(response.status_code, 400)

    def test_edit_profile(self):
        with app.test_client(self) as c:
            with c.session_transaction() as sess:
                sess["email"] = "shivakandhagatla1999@gmail.com"
                sess["password"] = "12345"
        response = c.post(
            "/edit_profile", data={"name": "Ramya Sai Mullapudi", "location": "NC"}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
