from flask import Flask
from flask import render_template, request, redirect
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index_khab', methods=['GET', 'POST'])
def index_khab():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect('/index')


@app.route('/about_us')
def about_us():
    return render_template('about.html')


@app.route('/map')
def map_html():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
