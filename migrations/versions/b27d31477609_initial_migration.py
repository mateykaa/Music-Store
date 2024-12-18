"""Initial migration

Revision ID: b27d31477609
Revises: 
Create Date: 2024-12-13 16:21:20.871845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b27d31477609'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ensembles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('wholesale_price', sa.Float(), nullable=True),
    sa.Column('retail_price', sa.Float(), nullable=True),
    sa.Column('sales_last_year', sa.Integer(), nullable=True),
    sa.Column('sales_current_year', sa.Integer(), nullable=True),
    sa.Column('quantity_available', sa.Integer(), nullable=True),
    sa.Column('ensemble_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ensemble_id'], ['ensembles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('musicians',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('instruments', sa.String(length=150), nullable=True),
    sa.Column('ensemble_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ensemble_id'], ['ensembles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('musicians')
    op.drop_table('albums')
    op.drop_table('ensembles')
    # ### end Alembic commands ###