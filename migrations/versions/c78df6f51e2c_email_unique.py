"""Email_unique

Revision ID: c78df6f51e2c
Revises: 5dc30fab059f
Create Date: 2024-03-22 14:07:49.862089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c78df6f51e2c'
down_revision: Union[str, None] = '5dc30fab059f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_contacts_email', table_name='contacts')
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.create_index('ix_contacts_email', 'contacts', ['email'], unique=False)
    # ### end Alembic commands ###