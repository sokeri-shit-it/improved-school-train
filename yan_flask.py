from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from form.users import RegisterForm

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
    return render_template('about-us.html')


@app.route('/map')
def map_html():
    return render_template('map.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_session.global_init('db/user_info.db')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
