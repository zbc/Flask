from app import app
from flask import render_template, redirect, flash
from forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    title = "Bo"
    user = {'nickname': 'Bo'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title = title, user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)
