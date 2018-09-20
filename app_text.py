from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col

import os
from model_udb import db_session, User
from sqlAlchemy_insert import gender_user_by_id
# Some application and database setup. This should be taken care of
# elsewhere in an application and is not specific to the tables. See
# Flask-SQLAlchemy docs for more about what's going on for this first
# bit.
from tables import Results

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('pages/lk/train.html')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=4000)