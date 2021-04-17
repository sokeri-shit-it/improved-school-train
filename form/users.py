from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    city = StringField('Ваш город', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class EditProfileForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    city = StringField('Ваш город', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class DeliveryForm(FlaskForm):
    username = StringField('Имя отправителя', validators=[DataRequired()])
    email = StringField('Ваша почта', validators=[DataRequired()])

    delivery_city = StringField('Город отправки', validators=[DataRequired()])
    forwarding_city = StringField('Город доставки', validators=[DataRequired()])

    forwarding_mail_city = IntegerField('Почтовый индекс (города отправки)')
    delivery_mail_city = IntegerField('Почтовый индекс (города отправки)')
    
    order_message = StringField('Сообщение к заказу')

    submit = SubmitField('Сделать заказ')


class TrackForm(FlaskForm):
    random_order_code = IntegerField('Введите код для отслеживания:')

    submit = SubmitField('Получить данные')
     