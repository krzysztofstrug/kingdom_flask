from flask import Flask, render_template

#flask instance
app = Flask(__name__)

# route decorator
@app.route('/')
def index():
    my_name = 'Krzysztof'
    stuff = "This is <strong>Bold</strong> text"
    favorite_pizza = ["peperoni", "cheese", "test", 41]
    return render_template("index.html",
        my_name=my_name,
        stuff=stuff,
        favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Custom Error pages
# http 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
# http 500
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
