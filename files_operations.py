from flask import Blueprint

files_operations = Blueprint('flask_operations', __name__)


@files_operations.route('/file/create/<path:filename>', methods=['POST'])
def create(filename):
    if request.method == 'POST':
        pass


@files_operations.route('/file/read/<path:filename>')
def read(filename):
    return f'{filename}'


@files_operations.route('/file/write/<path:filename>', methods=['POST'])
def write(filename):
    pass


@files_operations.route('/file/delete/<path:filename>')
def delete(filename):
    pass


@files_operations.route('/file/info/<path:filename>')
def info(filename):
    pass


@files_operations.route('/file/copy/<path:filename>')
def copy(filename):
    pass


@files_operations.route('/file/info/<path:filename>')
def move(filename):
    pass
