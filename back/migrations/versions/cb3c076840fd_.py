"""empty message

Revision ID: cb3c076840fd
Revises: 0a0ad0bbc696
Create Date: 2022-11-04 15:54:04.167867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb3c076840fd'
down_revision = '0a0ad0bbc696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('type_cryptage', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'type_cryptage')
    # ### end Alembic commands ###