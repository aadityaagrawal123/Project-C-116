# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

@app.route("/")
def home():

    name = "Aaditya Agrawal"
    age = "14"

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():
    name = "Narendra Agrawal"
    age = "42"

    return render_template('father.html' , name = name , age = age)

@app.route("/mother")
def mother():
    name = "Krishna Agrawal"
    age = "38"

    return render_template('mother.html' , name = name , age = age)

@app.route("/friend")
def friend():
    name = "Gopal"
    age = "14"

    return render_template('friend.html' , name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
