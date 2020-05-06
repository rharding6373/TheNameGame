# The Name Game
# Player inputs their name and the name they want another player to guess.
# Once all players have submitted, assign names to players.
# Display assignments to players, omitting that player's assignment.

import logging
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Name Game!"

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
