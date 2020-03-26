"""empty message

Revision ID: 77985ac6986d
Revises: 
Create Date: 2020-03-26 14:02:22.157774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77985ac6986d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('zadanie_id', sa.Integer(), nullable=False),
    sa.Column('tresc_zadania', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('zadanie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
