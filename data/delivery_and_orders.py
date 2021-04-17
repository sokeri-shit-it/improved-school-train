import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from flask_login import UserMixin


class Delivery_and_Orders(SqlAlchemyBase, UserMixin):
    __tablename__ = 'delivery_and_orders'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    forwarding_city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    delivery_city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)

    order_message = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    forwarding_mail_adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    delivery_mail_adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    random_order_code = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    # order_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # save_order_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)


    created_date = sqlalchemy.Column(sqlalchemy.Date,
                                     default=datetime.date.today())

