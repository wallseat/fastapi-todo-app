"""change datetime fields to string

Revision ID: b1a20969838c
Revises: 40707756e270
Create Date: 2022-03-25 13:04:18.796348

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b1a20969838c"
down_revision = "40707756e270"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("todo", "created_at", type_=sa.String(96))
    op.alter_column("todo", "expires_at", type_=sa.String(96))


def downgrade():
    op.drop_column("todo", "expires_at")
    op.drop_column("todo", "created_at")
    op.add_column("todo", sa.Column("created_at", sa.DateTime(True)))
    op.add_column("todo", sa.Column("expires_at", sa.DateTime(True)))
