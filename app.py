from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://local_user:Password1@localhost:5432/sql_alchemy', echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
'''
person = Person()
person.id = 0
person.username = "alice"

session.add(person)
session.commit()
'''


people = session.query(Person).all()

for person in people:
    print('Person with username = %s and id = %d' % (person.username, person.id))

session.close()




