# All imports
from flask import Flask, render_template, request
import pymysql
from dynaconf import Dynaconf
import flask_login
import requests

# Declare Flask application
app = Flask(__name__)


# Config settings and secrets
conf = Dynaconf(
    settings_file = ["settings.toml"]
)

# Establish database connection
def connect_db():
    """Connect to the phpMyAdmin database (LOCAL STEAM NETWORK ONLY)"""
    conn = pymysql.connect(
        host = conf.host,
        database = conf.db,
        user = conf.user,
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
    
# Load User Session
@login_manager.user_loader
def load_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `user` WHERE `id` = {id};")
    result = cursor.fetchone()
    cursor.close()
    conn.close
    if result is not None:
        return User(result["id"], result["username"], result["email"], result["name"])

# Homepage initialization
@app.route("/")
def homepage():
    return("homepage.html.jinja")

if __name__ == '__main__':
    app.run(debug=True)

# Browse colleges
@app.route("/browse")
def college_browse():
    query = request.args.get("query")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `College`;")
    colleges = cursor.fetchall()
    return render_template("browse.html.jinja", results = colleges)

## User account system

## Search system
def requestinfo(schoolname='', schoolstate=''):
    count = 0
    api="https://api.data.gov/ed/collegescorecard/v1/schools?api_key=fEZsVdtKgtVU4ODIpjHcP8vDttDK0ftSGZaWDcAk"
    queries={}
    request=''
    if schoolname:
        queries.update({"school.name":(f"{schoolname}")})
    
    if schoolstate:
        queries.update({"school.state":(f"{schoolstate}")})

    for query in queries:
        request+=(f"{query}={queries[query]}")
        count+=1
    
    request=f"{api}&{request}"

    test= requests.get(request).json()

    for key in test:{ 
        print(key,":", test[key]) 
    }
        
    return request

print(requestinfo("Harvard University"))
