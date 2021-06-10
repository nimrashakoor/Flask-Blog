import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/projects/')
def projects():
    return render_template('projects.html', title="Projects")


@app.route('/blog/')
def blog():
    return render_template('blog.html', title="Blog")


@app.route('/contact/')
def contact():
    return render_template('contact.html', title="Contact")
