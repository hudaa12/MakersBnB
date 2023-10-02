MakersBnB
In this group project, we were tasked with designing and integrating a SQL database in Python to create a web application called MakersBnB within 4 days.

MakersBnB is an AirBnB replica web application where you can register as a user, log-in as a user, and find and book accomodation or offer accomodation to be booked.


```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit http://localhost:5000/index in your browser
```# Makers_BnB
