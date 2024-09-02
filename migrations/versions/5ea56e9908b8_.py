"""empty message

Revision ID: 5ea56e9908b8
Revises: 6a587d654593
Create Date: 2024-09-02 04:24:32.625739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea56e9908b8'
down_revision = '6a587d654593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.String(length=120), nullable=False),
    sa.Column('orbital_period', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('gravity', sa.String(length=120), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.Column('surface_water', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###