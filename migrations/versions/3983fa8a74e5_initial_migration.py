"""Initial migration

Revision ID: 3983fa8a74e5
Revises: 
Create Date: 2024-01-12 02:03:20.793670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3983fa8a74e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('estudante')
    # ### end Alembic commands ###
