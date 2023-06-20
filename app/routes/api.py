from flask import Blueprint, request, jsonify, session
# Allows for testging errors 
import sys
from app.models import User 
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    
    try:
        # Create new user
        newUser = User(
            # Use bracket notation becuase it's a Python Dictionary
            username = data['username'],
            email = data['email'],
            password = data['password'],
        )

        # Save in database
        db.add(newUser)
        db.commit()
    except: 
        print(sys.exec_info()[0])

        # For productions
        db.rollback()
        # insert failed, so send error to front-end
        return jsonify(message = 'Signup failed'), 500
    
    # Clears any existing session data
    session.clear()
    # Creates two new session properties: user_id to aid future queries, and boolean for conditional rendering 
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id = newUser.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
    # Remove session variables
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db() 

    try:
        user = db.query(User).filter(User.email == data['email']).one()

    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect credentials'), 400

    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400
        
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True
    
    return jsonify(id = user.id)
