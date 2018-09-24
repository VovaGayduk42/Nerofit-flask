from flask import Flask, flash, render_template, request, session, app
import os
from flask_sqlalchemy import SQLAlchemy
from Other.model_udb import *
from Other.sqlAlchemy_insert import user_add

from tables import Results

@app.route('/')
def login_page():
    return render_template('')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
