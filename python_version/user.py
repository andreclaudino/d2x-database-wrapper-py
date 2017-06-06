from flask import Blueprint, abort
from flask import jsonify

user_page = Blueprint('user', __name__)

@user_page.route('/user')
@user_page.route('/')
def show():
    return jsonify({"result" : "ok"})

