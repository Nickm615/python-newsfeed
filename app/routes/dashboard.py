from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db
from app.utils.auth import login_required
# we use url_prefix to add /dashboard to the start of each of our routes inside this file
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/')
@login_required
def dash():
    db = get_db()
    #to break up this lengthy query we must wrap it in parens to avoid a python indentation error
    posts = (
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template(
      'dashboard.html',
      posts=posts,
      loggedIn=session.get('loggedIn')
      
      )


@bp.route('/edit/<id>')
@login_required
def edit(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render edit page
  return render_template(
    'edit-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )