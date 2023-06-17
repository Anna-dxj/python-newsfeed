# Only care about the bp object because other functions are already attached ot it with @bp.route() decorator
# .home directs program to module
# Import bp object as "home" 
from .home import bp as home
from .dashboard import bp as dashboard