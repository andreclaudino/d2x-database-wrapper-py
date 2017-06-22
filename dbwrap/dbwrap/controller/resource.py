from flask import Blueprint, abort
from flask import jsonify

route = Blueprint('resource', __name__)

@route.route('/resource')
@route.route('/')
def show():
    return jsonify({"result" : "ok"})

