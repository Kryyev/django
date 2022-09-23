import sqlite3
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def data():
    return render_template('index.html')


def conn():
    connection = sqlite3.connect('example.sqlite3')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/tracks/list/<int:count>')
def best_tracks(count):
    connection = conn()
    tracks = connection.execute('select * from trackks ').fetchmany(count)
    connection.close()
    return render_template('index.html', tracks=tracks)


if __name__ == ('__main__'):
    app.run(debug=True, port=5020)