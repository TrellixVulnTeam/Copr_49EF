"""empty message

Revision ID: 1ee4b45f5476
Revises: 3a035889852c
Create Date: 2013-02-14 14:11:50.624673

"""

# revision identifiers, used by Alembic.
revision = "1ee4b45f5476"
down_revision = "3a035889852c"

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("copr", u"copr_ts_col")
    if op.get_bind().dialect.name == "postgresql":
        op.execute("DROP trigger IF EXISTS copr_ts_update ON copr")
    elif op.get_bind().dialect.name == "sqlite":
        op.execute("DROP trigger IF EXISTS copr_ts_update")
        op.execute("DROP trigger IF EXISTS copr_ts_insert")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column("copr", sa.Column(u"copr_ts_col", sa.TEXT(), nullable=True))
    ### end Alembic commands ###
