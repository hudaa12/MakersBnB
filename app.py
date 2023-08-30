import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.spaces_repository import SpacesRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index


@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/space', methods=['GET'])
def get_space():
    return render_template('index_space.html')

@app.route('/space', methods=['POST'])
def list_space():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection) 
    name = request.form['space_name']
    description = request.form['description']
    price = request.form['price']
    available_from = request.form['available_from']
    available_to = request.form['available_to']
    user_id = request.form['user_id']

    space = Space(None, name, description, price, available_from, available_to, user_id) 
    repository.create(space)

    return render_template('index_space.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
