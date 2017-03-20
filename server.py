from flask import Flask, request, session
from random import choice


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    #session['count'] = 222;
    #str(session['count'];
    

    return """<html>
    <body>
    <h1>Hello! Do you choose rock, paper or scissors?</h1>
    <p><h2>
    <p> <img src="https://media.giphy.com/media/14ty7Uk1T7jo5O/giphy.gif"></p>
    <p>
    <a href="http://127.0.0.1:5000/rock">ROCK!</a></p>
    <p>
    <a href="http://127.0.0.1:5000/paper">PAPER!</a></p>
    <p>
    <a href="http://127.0.0.1:5000/scissors">SCISSORS!</a></p></h2>

    </body></html>"""

def tie():
    return """<html>
    <body>
    <h1>Tie!!!</h1>
    <p> <img src="http://www.gifmania.co.uk/Objects-Animated-Gifs/Animated-Toys/Rock-Paper-Scissors/Rock-Paper-Scissors-87021.gif"></p>
    <p><h2>Play again! Do you choose rock, paper or scissors?</p>
    <p>
    <a href="http://127.0.0.1:5000/rock">ROCK!</a></p>
    <p>
    <a href="http://127.0.0.1:5000/paper">PAPER!</a></p>
    <p>
    <a href="http://127.0.0.1:5000/scissors">SCISSORS!</a></p></h2>

    </body></html>"""

def who_won(player_a_choice, player_b_choice):
    if player_b_choice == player_a_choice:
        return 0

    elif player_a_choice == "Rock" and player_b_choice == "Paper":
        return "b" 

    elif player_a_choice == "Rock" and player_b_choice == "Scissors":
        return "a" 

    elif player_a_choice == "Scissors" and player_b_choice == "Paper":
        return "a"  

    elif player_a_choice == "Paper" and player_b_choice == "Scissors":
        return "b" 

    elif player_a_choice == "Scissors" and player_b_choice == "Rock":
        return "b"  

def play(user_choice):
    rock_paper_scissors = ("Rock", "Paper", "Scissors")
    computer_choice = choice(rock_paper_scissors)
    message_for_player = "You you entered %s. Computer had %s." % (user_choice, computer_choice)

    if who_won(user_choice, computer_choice) == 'a':
        win_message = "You won!" 

    elif who_won(user_choice, computer_choice) == 'b':
        win_message = "You lose!"

    elif computer_choice == user_choice:
        return tie()

    return """<html>
    <body>
    <h1>""" + message_for_player + " " + win_message + """ </h1>
    <h1>
    <p>
    <a href="http://127.0.0.1:5000/">Play again!!</a></p>
    </body></html>"""


@app.route('/rock')
def rock():
    return play("Rock")

@app.route('/paper')
def paper():
    return play("Paper")

@app.route('/scissors')
def scissors():
    return play("Scissors")

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.secret_key = 'OMNOMNOMNOM';
    app.run(debug=True)
