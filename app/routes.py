from app import app
from datetime import date
from .load_json import Assets
from flask import render_template
from flask import Markup


# TODO: USE DB instead of json
def posts_processing(posts):
    for post in posts:
        post["date"] = date.fromisoformat(post["date"])
        post["body"] = Markup(post["body"])
posts = Assets(src="app/static/assets/posts/")
posts.load_asset(processing=posts_processing)

def portfolio_processing(portfolio_samples):
    for sample in portfolio_samples:
        sample["date"] = date.fromisoformat(sample["date"])
        sample["body"] = Markup(sample["body"])
portfolio_samples = Assets(src="app/static/assets/portfolio/")
portfolio_samples.load_asset(processing=portfolio_processing)


@app.route('/')
@app.route('/index')
def index():
    return render_template("blog.html" ,title="Blog", posts=posts.load_recent(10))


# Converting date from datetime to string
app.add_template_global(lambda x: x.strftime("%Y %b %-d"), name="blog_date")
@app.route('/blog')
def blog():
    return render_template("blog.html" ,title="Blog", posts=posts.load_recent(10))

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html" ,title="Portfolio", samples=portfolio_samples.load_recent(10))

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")
