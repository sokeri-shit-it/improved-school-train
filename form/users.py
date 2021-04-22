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
    username = StringField('ФИО:', validators=[DataRequired()])
    email = StringField('Ваша почта (для отправки кода):')

    delivery_city = StringField('Город отправки:', validators=[DataRequired()])
    forwarding_city = StringField('Город доставки:', validators=[DataRequired()])
    
    order_message = StringField('Примечание к заказу:', validators=[DataRequired()])

    submit = SubmitField('Сделать заказ')


class TrackForm(FlaskForm):
    random_order_code = IntegerField('Введите код:')

    submit = SubmitField('Получить данные')
     