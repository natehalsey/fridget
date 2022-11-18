"""

Revision ID: 8723b6f2217a
Revises: 765ac83a6d0b
Create Date: 2022-11-18 09:49:51.134297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8723b6f2217a'
down_revision = '765ac83a6d0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ingredient', sa.Integer(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient'], ['ingredients.id'], name='fk_users_ingredients_ingredients_ingredient_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], name='fk_users_ingredients_users_user_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table(
        "recipes",
        reflect_args=[sa.Column('flag', sa.Boolean(create_constraint=True))],
    ) as batch_op:
        batch_op.add_column(sa.Column('saved_by', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_recipes_users_id_created_by', 'recipes', type_='foreignkey')
    op.drop_table('users_ingredients')
    # ### end Alembic commands ###