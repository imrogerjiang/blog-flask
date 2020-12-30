# export FLASK_APP=blog.py
# flask run

from app import app
from .posts import load_recent
from flask import render_template
from flask import Markup

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


# Converting date from datetime to string
app.add_template_global(lambda x: x.strftime("%Y %b %-d"), name="blog_date")
@app.route('/blog')
def blog():
    return render_template("blog.html" ,title="Blog", posts=load_recent(10))

@app.route('/portfolio')
def portfolio():
    return "Portfolio!~"

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")