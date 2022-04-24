"""Добавили новое поле в orders

Revision ID: 51d787da84a3
Revises: 949d4fd755c4
Create Date: 2021-04-23 21:22:57.915766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51d787da84a3'
down_revision = '949d4fd755c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delivery_and_orders', sa.Column('name', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'delivery_and_orders', ['random_order_code'])
    op.drop_constraint(None, 'delivery_and_orders', type_='foreignkey')
    op.create_foreign_key(None, 'delivery_and_orders', 'users', ['name'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'delivery_and_orders', type_='foreignkey')
    op.create_foreign_key(None, 'delivery_and_orders', 'users', ['username'], ['name'])
    op.drop_constraint(None, 'delivery_and_orders', type_='unique')
    op.drop_column('delivery_and_orders', 'name')
    # ### end Alembic commands ###
