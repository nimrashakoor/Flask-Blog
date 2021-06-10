import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    projects = []
    projects.append({'name':'Tracking fruit growth', 'date':'06/11/2021', 'descrip':
    ['my project is cool', 'it is so cool']})
    projects.append({'name':'proj1', 'date':'06/11/2021', 'descrip':['my project is cool', 'it is so cool']})

    images = []
    images.append('/static/img/safari_tree.jpg')
    return render_template('projects.html', projs=projects, imgs=images, url=os.getenv("URL"))
