from flask import Flask
from app.routes import home, dashboard
from app.db import init_db

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
  # Decorator (@app.route) extends our hello function without explicitly changing it, turning it into a route and making the content it returns into a response.
  @app.route('/hello')
  def hello():
    return 'hello world'
    # Registers the imported route blueprint named "home"
  app.register_blueprint(home)
  app.register_blueprint(dashboard)


  init_db(app)
  return app