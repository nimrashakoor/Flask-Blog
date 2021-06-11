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
    projects.append({'name':'Tracking the Population Growth of Baobab Trees', 'date':'00/00/0000', 'descrip':
    ['Baobab trees are endangered, partially due to drought, and tracking their growth is vital as many animals depend on them to survive',
    'All data utilized is primary'], 'img':['/static/img/baobab_tree.jpg', 'Baobab Tree'], 'link':'https://github.com/JocelynHeckenkamp/Flask-Blog'})
    projects.append({'name':'Mobile App for Navigating the Safari', 'date':'00/00/0000',
    'descrip':['Utilizes a shortest-path algorithm for leaving the jungle', 'Has an option for avoiding waterholes'],
    'img':['/static/img/travelling.jpg', 'Travelling through the Safari'], 'link':'https://github.com/JocelynHeckenkamp/Flask-Blog'})
    projects.append({'name':'Finding Ancestry of Safari Animals', 'date':'00/00/0000',
    'descrip':['Uses DNA data to trace the history of safari animals as we know them today',
    'Support for other biomes is currently in the works'],
    'img':['/static/img/rhinos.jpg', 'Travelling through the Safari'], 'link':'https://github.com/JocelynHeckenkamp/Flask-Blog'})
    return render_template('projects.html', projs=projects, url=os.getenv("URL"))

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")
