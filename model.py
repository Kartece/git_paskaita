from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Order(Base):
    id = Column(Integer, primary_key=True)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

