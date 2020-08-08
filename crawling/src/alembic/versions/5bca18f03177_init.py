"""init

Revision ID: 5bca18f03177
Revises: 5a585fdb9579
Create Date: 2020-08-08 02:51:11.998060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bca18f03177'
down_revision = '5a585fdb9579'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notices',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('site', sa.String(length=30), nullable=True),
    sa.Column('is_fixed', sa.Boolean(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('author', sa.String(length=30), nullable=True),
    sa.Column('reference', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notices')
    # ### end Alembic commands ###
