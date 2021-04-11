from flask import Flask

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = "/home/roger/code/blog-html"

from app import routes
