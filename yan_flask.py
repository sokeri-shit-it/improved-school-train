from flask import Flask
from flask import render_template
import jinja2

app = Flask(__name__)


@app.route('/index_khab')
def index_khab():
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    return render_template('about.html')


@app.route('/map')
def map_html():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
