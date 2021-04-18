# import Flask

from flask import Flask

#define flask app define welcome route

app = Flask(__name__)
@app.route("/")
def welcome():
    return("Hello World")

# Define the about route

# @app.route('/')


if __name__ == "__main__":
    app.run(debug = True)



    