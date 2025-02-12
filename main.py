from flask import Flask, render_template
import pymysql
from dynaconf import Dynaconf
import flask_login

# Declare Flask application
app = Flask(__name__)


# Config settings
conf = Dynaconf(
    settings_file = ["settings.toml"]
)



# Establish database connection
def connect_db():
    """Connect to the phpMyAdmin database (LOCAL STEAM NETWORK ONLY)"""
    conn = pymysql.connect(
        host = "db.steamcenter.tech",
        database = "apollo",
        user = "fchowdury",
        password = conf.password,
        autocommit = True,
        cursorclass = pymysql.cursors.DictCursor
    )
    return conn

# User Login Manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view=("/login")

# Classes
class User:
    is_authenticated = True
    is_anonymous = False
    is_active = True

    def __init__(self, user_id, username, email, first_name, last_name):
        self.id = user_id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return str(self.id)

# Homepage initialization
@app.route("/")
def index():
    return render_template("homepage.html.jinja")