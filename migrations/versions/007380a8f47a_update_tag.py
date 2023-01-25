"""update tag

Revision ID: 007380a8f47a
Revises: e1b43436d418
Create Date: 2023-01-25 17:40:48.769616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '007380a8f47a'
down_revision = 'e1b43436d418'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_model')
    # ### end Alembic commands ###