import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.users_repository import UsersRepository
from lib.users import Users

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index


@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def new_user_created():
    connection = get_flask_database_connection(app)
    repository = UsersRepository(connection)

    email = request.form['email']
    password = request.form['password']
    user = Users(None, email, password)
    repository.new_user_created(user)

    return render_template('/index.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
