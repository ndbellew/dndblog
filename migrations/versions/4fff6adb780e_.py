"""empty message

Revision ID: 4fff6adb780e
Revises: 7773c4a4c112
Create Date: 2021-01-13 21:17:40.100690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fff6adb780e'
down_revision = '7773c4a4c112'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('followers', sa.Column('followed_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'followers', 'user', ['followed_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.drop_column('followers', 'followed_id')
    # ### end Alembic commands ###
