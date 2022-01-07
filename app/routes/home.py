from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db
# Blueprint lets us consolidate routes into a single bp object (like using Router middleware of Express.js)
bp = Blueprint('home', __name__, url_prefix='/')

# We use @bp decorator with our index, login, and single post functions to turn them into routes. These functions return templates from our templates folder as a response.
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  return render_template(
    'homepage.html',
    posts=posts
    )

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  # Filter is equivalent to SQL WHERE
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
    'single-post.html',
    post=post
  )