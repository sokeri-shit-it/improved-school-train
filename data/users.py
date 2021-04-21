import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.Date,
                                     default=datetime.date.today())

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Delivery_and_Orders(SqlAlchemyBase, UserMixin):
    __tablename__ = 'delivery_and_orders'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    
    forwarding_city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    delivery_city = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    order_message = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    forwarding_mail_adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    delivery_mail_adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    random_order_code = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.Date,
                                     default=datetime.date.today())