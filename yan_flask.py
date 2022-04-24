import os
import sys
import random
import requests
import sqlalchemy
import smtplib

from data import db_session
from threading import Thread
from flask_mail import Mail, Message
from flask_script import Manager, Shell
from data.users import User, Delivery_and_Orders
from flask import Flask, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form.users import RegisterForm, LoginForm, EditProfileForm, DeliveryForm, TrackForm


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'khabexpress@gmail.com'
app.config['MAIL_PASSWORD'] = 'lolo3322'
app.config['MAIL_DEFAULT_SENDER'] = 'khabexpress@gmail.com'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)


@login_manager.user_loader
def load_user(user_id):
    db_session.global_init('db/user_info.sqlite')
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
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
        db_session.global_init('db/user_info.sqlite')
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
        db_session.global_init('db/user_info.sqlite')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=register_form.remember_me.data)
            return redirect("/")
        else:
            return render_template('login.html', message='Неправильный пароль', form=form)
        return render_template('login.html',
                               message="Неправильный логин ",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/profile')
@login_required
def account():
    db_session.global_init('db/user_info.sqlite')
    db_secc = db_session.create_session()
    order_id = db_secc.query(Delivery_and_Orders).all()
    return render_template('account.html', order_id=order_id)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    login = LoginForm()
    db_session.global_init('db/user_info.sqlite')
    db_sess = db_session.create_session()
    user = db_sess.query(User).order_by(sqlalchemy.desc(User.id)).first()
    print(user.name)
    if form.validate_on_submit():   
        user.name = form.username.data
        user.city = form.city.data
        user.hashed_password = generate_password_hash(form.password.data)
        user.email = form.email.data
        db_sess.commit()
        return redirect('/profile')
    elif request.method == 'GET':
        form.username.data = user.name
        form.email.data = user.email 
        form.city.data = user.city
    return render_template('settings.html', form=form)


@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    form = DeliveryForm()
    
    if form.validate_on_submit():
        db_session.global_init('db/user_info.sqlite')
        db_secc = db_session.create_session()
        
        order = Delivery_and_Orders(
            email=form.email.data,
            username=form.username.data,
            # name=User.name,
            delivery_city=form.delivery_city.data,
            forwarding_city=form.forwarding_city.data,  
            order_message=form.order_message.data,
            random_order_code=random.randint(1000, 10000)
        )

        message = Message(f"Здравствуйте {form.username.data}!", recipients=[form.email.data])
        message.html = render_template('mail.html', form=form, order=order)
        mail.send(message)

        db_secc.add(order)
        db_secc.commit()

        return render_template('window.html', form=form)
    return render_template('delivery.html', form=form)


@app.route('/track_delivery', methods=['GET', 'POST'], endpoint='track_delivery')
def track_order():
    form = TrackForm()
    db_session.global_init('db/user_info.sqlite')
    db_secc = db_session.create_session()
    cities = db_secc.query(Delivery_and_Orders).filter(Delivery_and_Orders.random_order_code == form.random_order_code.data).first()
    if form.validate_on_submit():
        if cities:
            os.environ['no_proxy'] = '127.0.0.1,localhost'
            get_forward_city = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={cities.forwarding_city}&format=json"
            get_delivery_city = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={cities.delivery_city}&format=json"

            for_responce, del_responce = requests.get(get_forward_city), requests.get(get_delivery_city)

            for_response_json, del_response_json = for_responce.json(), del_responce.json()

            toponym1 = for_response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            meta_coords1 = toponym1["metaDataProperty"]["GeocoderMetaData"]["text"]
            coords1 = toponym1["Point"]["pos"]

            toponym2 = del_response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            meta_coords2 = toponym2["metaDataProperty"]["GeocoderMetaData"]["text"]
            coords2 = toponym2["Point"]["pos"]

            api_server = "http://static-maps.yandex.ru/1.x/"

            lon = str((float(coords1.split(' ')[0]) + float(coords2.split(' ')[0])) / 2)
            lat = str((float(coords1.split(' ')[1]) + float(coords2.split(' ')[1])) / 2)
            delta = "10"

            params = {
                "ll": ",".join([lon, lat]),
                "spn": ",".join([delta, delta]),
                "l": "map",
            }
            response = requests.get(api_server, params=params)

            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            map_file = "static/img/map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
    db_secc.commit()

    return render_template('track.html', form=form, cities=cities)
    


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
     