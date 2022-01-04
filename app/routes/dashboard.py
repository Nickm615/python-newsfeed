from flask import Blueprint, render_template
# we use url_prefix to add /dashboard to the start of each of our routes inside this file
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')