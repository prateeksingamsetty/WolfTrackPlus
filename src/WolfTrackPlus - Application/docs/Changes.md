# Changes in project phase 3
## Bugs Squashed:

1. Navigation bar issue fixed where clicking the logo logs out the user, we have added functionality to redirect to the user dashboard
2. Logout functionality was not working. There was no concept of sessions, and logout was a stub, we implemented the sessions and probperly handled the login and logout of users.
3. Each section of Application status was not being populated.
4. Sign-up was not working and was throwing an exception to the user.

## Enhancements:
1. Only adding an application was supported, we could not modify the application details once added, we added feature to edit the application.
2. Change the application status, to any other status seamlessly from the dashboard.
3. Delete an application from the dashboard to remove unnecessary applications.
4. Having too many applications, clutters the dashboard, we have cleaned up the interface by adding scrollbar for job listings on dashboard
5. Getting notified on your applications has never been easier, as you receive emails with your changes in applications and events.
6. Users can modify their profile using the edit profile operation present in the dashboard
7. Users are now greeted with a whole new overhaul of the user-interface with new UI elements and easy to understand icons.
8. Now application is accessible to everyone via your phone, computer or tablet, as our website is now hosted on the website - http://rjprabhu.pythonanywhere.com/
9. Added a fresh new documentation for the entire code base to help new developers and existing developers understand more about the apis and the code base.
10. Added new GitHub actions to automatically test code
11. Implemented and improved code coverage with extensive tests for all the components.
12. Used standard practices for code formatting with black with GitHub actions verifying it with every commit.
13. Cleaned up code base where unused an unnecessary files were created.
14. Updated security flaws, where passwords were sent to the users.