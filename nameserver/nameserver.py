from sqlite3 import connect, Error
from os import path
from flask import Flask, request, redirect, url_for
from files_operations import files_operations
from directories_operations import dir_operations
from Database import Manager


app = Flask(__name__)

# Blueprints
app.register_blueprint(files_operations)
app.register_blueprint(dir_operations)


@app.route('/')
@app.route('/index')
def index():
    return '''
        hello
        <form method="post" action="/init">
            <input type="submit" value="init">
        </form>
    '''


@app.route('/init', methods=['POST'])
def init():
    if request.method == 'POST':
        return redirect(url_for('index'))


@app.route('/get_hirerachy')
def get_hirerachy():
    pass


manager = Manager()
app.run()
