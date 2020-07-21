from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)


def open_connection(self):
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection, sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection


def execute_sql(self, sql, values, commit, single):
    connection = open_connection()
    values = ()
    commit = False
    single = False
    cursor = connection.execute(sql, values)
    if commit is True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
        cursor.close()
        return results


@app.teardown_appcontext
def close_connection(self, exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs(self):
    return render_template('index.html')
