from flask import Blueprint, abort
from flask import jsonify

resource_page = Blueprint('resource', __name__)

@resource_page.route('/resource')
@resource_page.route('/')
def show():
    return jsonify({"result" : "ok"})

