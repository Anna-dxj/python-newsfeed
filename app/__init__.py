# Import Flask() function
from flask import Flask
# Import home directly from routes package because its __init__.py file imported and renamed bp 
from app.routes import home, dashboard
from app.db import init_db 

# def keyword defines function 
def create_app(test_config=None):
    # setup app config without use of `const` or `var`
    # App serve any static resource from root directory instead of default `/static` directory
    app = Flask(__name__, static_url_path='/')
    # Make trailing slashes optional `/dashboard` and `/dashboard/` are the same
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        # Use key when creating server-side sessions
        SECRET_KEY='super_secret_key'
    )
    
    # Decorator that turns hell0() into a route
    @app.route('/hello')
    # Inner function that returns a string 
    def hello(): 
        return 'hello world'
    
    # Register the routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    # Initializes database 
    init_db(app)
    
    return app