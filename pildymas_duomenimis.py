from model import Order, User, sessionmaker, engine

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()

def edit_user(user_id, name, email):
    user = session.query(User).filter_by(id=user_id).first()
    user.name = name
    user.email = email
    session.commit()
