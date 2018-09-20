import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, Session
from models import User, engine


def get_info(id):
    # if __name__ == "__main__":
        metadata = MetaData(bind=engine)

        users = Table('users', metadata, autoload=True)
        print('SqlAlchemy test')

        print("In session")
        user = users.select(users.c.id == id).execute().first()
        # print("user =", user)
        return user

def get_name(id):
    user = User.query.filter_by(id=id).first()
    return user.username




def get_password(id):
    user = User.query.filter_by(id=id).first()
    return user.password


