from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

app.run(debug=True, port=5000)
