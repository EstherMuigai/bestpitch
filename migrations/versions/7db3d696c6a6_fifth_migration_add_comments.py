"""Fifth Migration-Add Comments

Revision ID: 7db3d696c6a6
Revises: 5c35c2746827
Create Date: 2019-04-24 17:36:51.607277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7db3d696c6a6'
down_revision = '5c35c2746827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
