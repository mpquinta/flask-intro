"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'ugly', 'stinky', 'kakapoopoo', 'smelly']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>Hi! This is the home page.<br>
    <a href="/hello">Link to hello</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    print("test!")
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>

          Choose a compliment:<br>
          <input type="radio" name="compliment" value="awesome">
          <label for="awesome">Awesome</label><br>
          <input type="radio" name="compliment" value="terrific">
          <label for="terrific">terrific</label><br>
          <input type="radio" name="compliment" value="fantastic">
          <label for="fantastic">fantastic</label><br>
          <input type="radio" name="compliment" value="neato">
          <label for="neato">neato</label><br>
          <input type="radio" name="compliment" value="fantabulous">
          <label for="fantabulous">fantabulous</label><br>
          <input type="radio" name="compliment" value="wowza">
          <label for="wowza">wowza</label><br>
          <input type="radio" name="compliment" value="oh-so-not-meh">
          <label for="oh-so-not-meh">oh-so-not-meh</label><br>
          <input type="radio" name="compliment" value="brilliant">
          <label for="brilliant">brilliant</label><br>
          <input type="radio" name="compliment" value="ducky">
          <label for="ducky">ducky</label><br>
          <input type="radio" name="compliment" value="coolio">
          <label for="coolio">coolio</label><br>
          <input type="radio" name="compliment" value="incredible">
          <label for="incredible">incredible</label><br>
          <input type="radio" name="compliment" value="wonderful">
          <label for="wonderful">wonderful</label><br>
          <input type="radio" name="compliment" value="smashing">
          <label for="smashing">smashing</label><br>
          <input type="radio" name="compliment" value="lovely">
          <label for="lovely">lovely</label><br>

          <input type="submit" value="submit">
          
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def greet_person():
    """Insult the user."""

    player = request.args.get("person")

    insult = choice(INSULTS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
