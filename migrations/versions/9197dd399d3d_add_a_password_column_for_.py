"""add a password column for authentification

Revision ID: 9197dd399d3d
Revises: aa952a06483e
Create Date: 2020-07-25 14:05:41.272196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9197dd399d3d'
down_revision = 'aa952a06483e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
