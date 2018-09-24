from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker

from app import db

engine = create_engine('sqlite:///db_relation.db', echo=True)
metadata = MetaData()
db.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()


########################################################################
class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    gender = Column(String,default='1')
    data = Column(String,default='25')
    height = Column(String, default='170')
    activity = Column(String, default='1')
    massuser = Column(String,default='75')
    auth = Column(Boolean, default=False)

    user_info = relationship("user_info", backref='user')

    # user_infos = relationship('user_info')

    # ----------------------------------------------------------------------
    def __init__(self, username, password, gender, data, height, activity,massuser, auth):
        """"""
        self.username = username
        self.password = password
        self.gender = gender
        self.data = data
        self.height = height
        self.activity = activity
        self.massuser = massuser
        self.auth = auth

    def __repr__(self):
        return "<User(%r, %r)>" % (
            self.username, self.password
        )


class user_info(Base):
    query = db_session.query_property()
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    mass = Column(String)
    chest = Column(String)
    left_hand = Column(String)
    left_bedro = Column(String)
    left_golen = Column(String)
    waist = Column(String)
    buttock = Column(String)
    right_hand = Column(String)
    right_bedro = Column(String)
    right_golen = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_helper = Column(Integer)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship('User')


def __init__(self, mass, chest, left_hand, left_bedro, left_golen, waist, buttock, right_hand, right_bedro,
             right_golen):
    """"""
    self.mass = mass
    self.chest = chest
    self.left_hand = left_hand
    self.left_bedro = left_bedro
    self.left_golen = left_golen
    self.waist = waist
    self.buttock = buttock
    self.right_hand = right_hand
    self.right_bedro = right_bedro
    self.right_golen = right_golen


def __repr__(self):
    return "<user_info(%r, %r,%r, %r,%r, %r,%r, %r,%r, %r)>" % (
        self.mass,
        self.chest,
        self.left_hand,
        self.left_bedro,
        self.left_golen,
        self.waist,
        self.buttock,
        self.right_hand,
        self.right_bedro,
        self.right_golen
    )


# create tables
Base.metadata.create_all(engine)
