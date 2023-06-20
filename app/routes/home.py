# Imports functions Blueprint() and render_template() from Flask module
# Blueprint() allows for consolidating routes onto a single bp object that parent app can register later 
# bp corresponds to using the Router middleware of Express.js
from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db 

bp = Blueprint('home', __name__, url_prefix='/')

# Turns function index() into a route
@bp.route('/')
def index():
    # Gets session to acess database
    db = get_db()
    # Get posts
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    # render_templat() responds with a template
    return render_template(
        'homepage.html',
         posts=posts
    )

# Creates route using a parameter (<id>)
@bp.route('/post/<id>')
# Include parameter as a function parameter 
def single(id):
    db=get_db()
    # Get a single post by id
    post = db.query(Post).filter(Post.id == id).one()

    # Return single post template
    return render_template(
        'single-post.html',
        post=post
    )

# Turns function login() into a route 
@bp.route('/login')
def login():
    return render_template('login.html')
