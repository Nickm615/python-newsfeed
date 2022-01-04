from flask import Blueprint, render_template
# Blueprint lets us consolidate routes into a single bp object (like using Router middleware of Express.js)
bp = Blueprint('home', __name__, url_prefix='/')

# We use @bp decorator with our index and login functions to turn them into routes. These functions return templates from our templates folder using Jinja as a response.
@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')