# .home directs the program to find the module named home in our current dir. We import the bp, renaming it home.
from .home import bp as home
from .dashboard import bp as dashboard
from .api import bp as api
