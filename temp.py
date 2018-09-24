from app import models, db

u = models.User(username='python',password='python')
db.session.add(u)
db.session.commit()

from flask import render_template, redirect, flash

from app import app
from app.forms import LoginForm
