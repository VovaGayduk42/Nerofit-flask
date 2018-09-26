from app import models, db

u = models.User(username='qwerty',password='2a3b04nn')
db.session.add(u)
db.session.commit()

from flask import render_template, redirect, flash

from app import app
from app.forms import LoginForm
