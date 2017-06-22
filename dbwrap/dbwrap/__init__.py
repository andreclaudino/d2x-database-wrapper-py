from flask import Flask
from dbwrap.controller import user
from dbwrap.controller import resource

app = Flask(__name__)
app.register_blueprint(user.route)
app.register_blueprint(resource.route)
