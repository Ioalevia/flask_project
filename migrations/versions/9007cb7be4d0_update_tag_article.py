"""update tag article

Revision ID: 9007cb7be4d0
Revises: 007380a8f47a
Create Date: 2023-01-25 17:59:07.909610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9007cb7be4d0'
down_revision = '007380a8f47a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article_model.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag_model.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_association')
    # ### end Alembic commands ###