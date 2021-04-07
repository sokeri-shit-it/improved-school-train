import os

from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from form.users import RegisterForm, LoginForm, EditProfileForm
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_session.global_init('db/user_info.db')
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/index_khab")


@app.route('/index_khab')
def index_khab():
    return render_template('index.html', title='Главная страница KHAB EXPRESS')


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
            city=form.city.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    register_form = RegisterForm()
    if form.validate_on_submit():
        db_session.global_init('db/user_info.db')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=register_form.remember_me.data)
            return redirect("/index_khab")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/profile')
@login_required
def account():
    return render_template('account.html')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    db_session.global_init('db/user_info.db')
    db_sess = db_session.create_session()
    if form.validate_on_submit():
        User.name = form.username.data
        User.city = form.city.data
        User.hashed_password = generate_password_hash(form.password.data)
        User.email = form.email.data
        db_sess.commit()
        return redirect('/profile')
    elif request.method == 'GET':
        form.username.data = User.name
        form.email.data = User.email
    return render_template('settings.html', title='Edit Profile',
                           form=form)


@app.route('/delivery', methods=['GET', 'POST'])
@login_required
def delivery():
    return render_template('delivery.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
