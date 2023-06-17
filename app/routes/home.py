# Imports functions Blueprint() and render_template() from Flask module
# Blueprint() allows for consolidating routes onto a single bp object that parent app can register later 
# bp corresponds to using the Router middleware of Express.js
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# Turns function index() into a route
@bp.route('/')
def index():
    # render_templat() responds with a template
    return render_template('homepage.html')

# Turns function login() into a route 
@bp.route('/login')
def login():
    return render_template('login.html')

# Creates route using a parameter (<id>)
@bp.route('/post/<id>')
# Include parameter as a function parameter 
def single(id):
    return render_template('single-post.html')