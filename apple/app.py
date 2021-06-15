from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Apple"
    
    text = """While walking home from school, you see an old lady who offers you an apple."""

    choices = [
        ('accept',"You accept the apple."),
        ('reject',"You reject the apple.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/accept")
def enter_house():
    title = "You start eating the apple."
    
    text = """... this is the sweetest apple that you have ever eaten."""

    choices = [
        ('eat',"You keep eating the apple."),
        ('reject',"You stop eating the apple.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/reject")
def run_away():
    title = "You reject the apple."
    
    text = """You continue walking home like every other day."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("eat")
def up_stairs():
    title = "What's happening???"
    
    text = """ You turn into a worm. Now you will live a life with no worries inside an apple."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
