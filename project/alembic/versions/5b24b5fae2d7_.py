"""empty message

Revision ID: 5b24b5fae2d7
Revises: 
Create Date: 2021-11-04 23:04:46.358557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b24b5fae2d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('use_case', sa.String(length=100), nullable=True),
    sa.Column('date_of_creation', sa.DateTime(), nullable=True),
    sa.Column('secret', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_User_id'), 'User', ['id'], unique=False)
    op.create_table('crawled_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('html', sa.Text(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('email',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('value')
    )
    op.create_table('Url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shorten', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('redirect_to', sa.String(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Url_id'), 'Url', ['id'], unique=True)
    op.create_table('crawled2email',
    sa.Column('crawled_data_id', sa.Integer(), nullable=True),
    sa.Column('email_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['crawled_data_id'], ['crawled_data.id'], ),
    sa.ForeignKeyConstraint(['email_id'], ['email.id'], )
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(length=64), nullable=True),
    sa.Column('crawled_data_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['crawled_data_id'], ['crawled_data.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('value')
    )
    op.create_table('Entry',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url_id', sa.Integer(), nullable=True),
    sa.Column('full_user_agent', sa.String(), nullable=True),
    sa.Column('referer', sa.String(), nullable=True),
    sa.Column('os', sa.String(), nullable=True),
    sa.Column('browser', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['url_id'], ['Url.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Entry')
    op.drop_table('image')
    op.drop_table('crawled2email')
    op.drop_index(op.f('ix_Url_id'), table_name='Url')
    op.drop_table('Url')
    op.drop_table('email')
    op.drop_table('crawled_data')
    op.drop_index(op.f('ix_User_id'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
