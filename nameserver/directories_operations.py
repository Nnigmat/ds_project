from flask import Blueprint

dir_operations = Blueprint('dir_operations', __name__)


@dir_operations.route('/dir/open/<path:dirname>')
def open_dir(dirname):
    pass


@dir_operations.route('/dir/read/<path:dirname>')
def read_dir(dirname):
    pass


@dir_operations.route('/dir/make/<path:dirname>')
def make_dir(dirname):
    pass


@dir_operations.route('/dir/delete/<path:dirname>')
def delete_dir(dirname):
    pass
