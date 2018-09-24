from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('password', String(length=120)),
    Column('gender', String),
    Column('data', String),
    Column('height', String),
    Column('activity', String),
    Column('massuser', String),
    Column('auth', Boolean, default=ColumnDefault(False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['data'].create()
    post_meta.tables['user'].columns['gender'].create()
    post_meta.tables['user'].columns['height'].create()
    post_meta.tables['user'].columns['massuser'].create()
    post_meta.tables['user'].columns['password'].create()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['data'].drop()
    post_meta.tables['user'].columns['gender'].drop()
    post_meta.tables['user'].columns['height'].drop()
    post_meta.tables['user'].columns['massuser'].drop()
    post_meta.tables['user'].columns['password'].drop()
    post_meta.tables['user'].columns['username'].drop()
