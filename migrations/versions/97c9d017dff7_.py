"""empty message

Revision ID: 97c9d017dff7
Revises: 3c0daf93f6fd
Create Date: 2021-05-06 19:35:07.177647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97c9d017dff7'
down_revision = '3c0daf93f6fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('goal_id', name='goal_pkey')
    )
    # ### end Alembic commands ###