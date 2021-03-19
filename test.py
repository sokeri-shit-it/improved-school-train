from flask import Flask
from flask import url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'sokeri whom dont anybody know'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:pass@localhost/my_db'

db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['education'])
        print(request.form['file'])
        print(request.form['prof'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
