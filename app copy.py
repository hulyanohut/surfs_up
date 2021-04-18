#import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#create engine, reflect database

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link
session = Session(engine)



# import Flask
from flask import Flask

# Create an app
app = Flask(__name__)

# Define index route
@app.route('/')
def index()
    return 'Hello world'
# Define the about route
@app.route('/')

    export FLASK_APP=app.py
    flask run

