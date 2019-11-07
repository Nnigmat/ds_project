from flask import Blueprint

dir_operations = Blueprint('flask_operations', __name__)


@dir_operations.route('/dir/open/<path:dirname>')
def open(dirname):
    pass


@dir_operations.route('/dir/read/<path:dirname>')
def read(dirname):
    pass


@dir_operations.route('/dir/make/<path:dirname>')
def make(dirname):
    pass


@dir_operations.route('/dir/delete/<path:dirname>')
def delete(dirname):
    pass
