# importing modules from the Flask library
from flask import Flask, render_template

# creating an instance of the Flask class, providing __name__ as an argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "Your Name"  # Your name
    age = 15  # Your age (an example age)

    return render_template('index.html', name=name, age=age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Father's Name"  # Father's name
    age = 50  # Father's age (an example age)

    return render_template('father.html', name=name, age=age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Mother's Name"  # Mother's name
    age = 45  # Mother's age (an example age)

    return render_template('mother.html', name=name, age=age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Friend's Name"  # Friend's name
    age = 16  # Friend's age (an example age)

    return render_template('friend.html', name=name, age=age)

# add other routes, if you want

# run the file
if __name__ == '__main__':
    app.run(debug=True)
