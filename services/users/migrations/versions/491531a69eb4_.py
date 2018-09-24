"""empty message

Revision ID: 491531a69eb4
Revises: 
Create Date: 2018-09-24 10:12:01.870429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '491531a69eb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###