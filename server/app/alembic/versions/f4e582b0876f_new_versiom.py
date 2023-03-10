"""New versiom

Revision ID: f4e582b0876f
Revises: 81e8b414c8f9
Create Date: 2023-02-17 16:40:16.569846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e582b0876f'
down_revision = '81e8b414c8f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('element_cart_ibfk_1', 'element_cart', type_='foreignkey')
    op.create_foreign_key(None, 'element_cart', 'element_cart', ['cart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'element_cart', type_='foreignkey')
    op.create_foreign_key('element_cart_ibfk_1', 'element_cart', 'shopping_card', ['cart_id'], ['id'])
    # ### end Alembic commands ###

