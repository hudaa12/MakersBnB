import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection

from lib.space import Space
from lib.space_repository import SpaceRepository

from flask_session import Session
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.booking_repository import BookingRepository
from lib.booking import Booking


# Create a new Flask app
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index


@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/space', methods=['GET'])
def get_space():
    return render_template('space.html')


@app.route('/spaces/<int:id>')
def get_space_detail(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('book_space.html', space=space)


@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)  # add user=user


@app.route('/space', methods=['POST'])
def post_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    booked_by = session['user_id']
    name = request.form['space_name']
    description = request.form['description']
    price = request.form['price']
    available_from = request.form['available_from']
    available_to = request.form['available_to']

    space = Space(None, name, description, price,
                  available_from, available_to, booked_by)
    repository.create(space)
    return render_template('space.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    new_user = User(None, email, password)
    repository.create(new_user)

    if repository.check_user_login(email, password) == True:
        user = repository.find_by_email(email)
        session["user_id"] = user.id
        return redirect('/spaces')
    else:
        return redirect('/')


@app.route("/logout")
def logout():
    session["name"] = None
    return render_template('/login.html')


@app.route('/index', methods=['POST'])
def post_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    user = User(None, email, password)
    repository.create(user)

    return render_template('/index.html')


@app.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html')


@app.route('/request_to_book', methods=['POST'])
def create_booking():
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    booking_date = request.form['date']
    booked_by = session['user_id']
    space_id = int(request.form['space_id'])
    booking = Booking(None, booking_date, booked_by, space_id)
    repository.create_booking(booking)
    return redirect('/bookings')


@app.route('/bookings', methods=['GET'])
def get_bookings():
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    bookings = repository.all()
    return render_template('requests.html', bookings=bookings)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
