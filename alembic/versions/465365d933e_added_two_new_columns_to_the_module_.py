"""Added two new columns to the module table

Revision ID: 465365d933e
Revises: 557eef06651
Create Date: 2015-12-29 00:01:43.762169

"""

# revision identifiers, used by Alembic.
revision = '465365d933e'
down_revision = '557eef06651'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_module', sa.Column('enabled', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.add_column('tb_module', sa.Column('settings', mysql.TEXT(), server_default=sa.text('NULL'), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_module', 'settings')
    op.drop_column('tb_module', 'enabled')
    ### end Alembic commands ###
