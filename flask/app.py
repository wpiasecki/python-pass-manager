from flask import Flask


# install dependencies with `pip3 install Flask`
# create a flask virtualenv with `virtualenv flask`
# use `source bin/activate` to change virtualenv
# run the app with FLASK_APP=app.py flask run


app = Flask(__name__)


CARDS = {
  '1': { 'name' : 'google', 'username' : 'googleuser', 'password' : 'googlepass', 'url' : 'google.com' },
  '2': { 'name' : 'twitter', 'username' : 'twitteruser', 'password' : 'twitterpass', 'url' : 'twitter.com' },
  '3': { 'name' : 'github', 'username' : 'githubuser', 'password' : 'githubpass', 'url' : 'github.com' },
  '4': { 'name' : 'amazon', 'username' : 'amazonuser', 'password' : 'amazonpass', 'url' : 'amazon.com' },
}


@app.route('/')
def say_hello():
  return "root"


@app.route('/password-cards')
def password_cards():
  return CARDS


if __name__ == '__main__':
  app.run()


