from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my Website<h1>"

@app.route("/about")
def about():
    return "<h1>About Page<h1>"

#  Path Parameter strings

@app.route("/welcome/<name>")   
def welcome(name):
    return f"Welcome, {name}!"


@app.route("/welcome_2/<int:num>")
def welcome_2(num):
    return f"Welcome, Number {num}!"

if __name__ == "__main__":
    app.run(debug=True)