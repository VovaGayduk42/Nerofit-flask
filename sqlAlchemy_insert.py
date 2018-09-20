import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, Session
from models import User, engine, db_session

def user_add_to_table(table, username, password):
    # if __name__ == "__main__":
    metadata = MetaData(bind=engine)
    users = Table(table, metadata, autoload=True)
    con = engine.connect()
    con.execute(users.insert(), username=username, password=password)
    print('User adding to database:')

def user_add(class_name, username, password):
    user = class_name(username, password)
    db_session.add(user)
    db_session.commit()

def user_delete(id):
    db_session.query(User). \
        filter(User.id == id). \
        delete()
    db_session.commit()

def gender_user_by_id(id, gender):
    user = User.query.get(id)
    user.gender = gender
    db_session.commit()