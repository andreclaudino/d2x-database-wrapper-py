from flask import Blueprint, abort
from flask import jsonify

route = Blueprint('user', __name__)

@route.route('/user')

@route.route('/')
def show():
    return jsonify({"result" : "ok"})

