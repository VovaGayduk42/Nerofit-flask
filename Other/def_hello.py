from sqlalchemy.orm import sessionmaker

from Other.model_udb import User, db_session, create_engine

engine = create_engine('sqlite:///db_relation.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

jack = User('Jo', '42', '', '', '', '', '', False)
db_session.add(jack)

# jack.user_info = [
#     user_info(mass='121'),
# ]
db_session.add(jack)
db_session.commit()
# commit the record the database


# user = User("admin", "password","","","")
# db_session.add(user)
# db_session.commit()
