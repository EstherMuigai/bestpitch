"""Third Migration-Add Pitch Model

Revision ID: 19c0feac9d17
Revises: d508850ff230
Create Date: 2019-04-24 10:29:00.055879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c0feac9d17'
down_revision = 'd508850ff230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('secondname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.Column('pitch_title', sa.String(), nullable=True),
    sa.Column('pitch_content', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
