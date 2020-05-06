# The Name Game
# Player inputs their name and the name they want another player to guess.
# Once all players have submitted, assign names to players.
# Display assignments to players, omitting that player's assignment.

import logging
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Configure logging
if not app.testing:
    logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET','POST'])
def welcome():
    logging.info('Someone went home!');
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        return redirect(url_for('.join_game'))
    return render_template('home.html')

@app.route('/join_game', methods=['GET','POST'])
def join_game():
    logging.info('Invited to join game');
    return render_template('join_game.html')

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
