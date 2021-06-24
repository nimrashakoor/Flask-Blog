import os
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from . import db
from werkzeug.security import generate_password_hash
from app.db import get_db

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

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
    posts = []
    posts.append({'name':'A Great Day', 'date':'00/00/0000',
    'descrip': 'Today, I met an oxpecker at the watering hole. We do not have much in common, and yet, somehow, we \
    work so well together. Here is a picture of us!', 'img':['/static/img/oxpecker.jpg', 'Rhino and Oxpecker']})
    posts.append({'name':'Perissodactyls', 'date':'00/00/0000',
    'descrip': 'I was looking up my ancestry today and discovered I am related to perissodactyls, and so are horses and zebras. \
    I wonder if there are any apps out there that track lineage? I am sure others would like to know where they came from too!',
    'img':['/static/img/perissodactyls.jpg', 'Perissodactyls']})
    posts.append({'name':'Welcome to our Blog!', 'date':'06/11/2021',
    'descrip': 'We are so glad that you took the chance to read our blog! It was made using Flask, HTML, and CSS. \
    Let us know on the Contact page if you have any suggestions for improvements! We look forward to hearing from you.',
    'img':['/static/img/rhino_image.jpg', 'Rhino']})
    return render_template('blog.html', posts=posts, url=os.getenv("URL"))

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(
            subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender=mail_username, recipients=['ns924@cornell.edu'])
        mail.send(msg)
        return render_template("contact.html", success=True)

    return render_template("contact.html")

@app.route('/health', methods=['GET'])
def health():
    return "Health", 200

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
    
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    #TODO return a register page
    return "Register Page not yet implemented", 501

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418
    
    #TODO return a login page
    return "Login Page not yet implemented", 501

if __name__ == "__main__":
    app.run(host='0.0.0.0')
