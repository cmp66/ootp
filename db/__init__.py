from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory', echo=True)

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    team = Column(String(20))
    org = Column(String(10))
    league = Column(String(10))
    level = Column(String(10))
    dob = Column(String(15))
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    bats = Column(String(10))
    throws = Column(String(10))
    leader = Column(String(10))
    loyalty = Column(String(10))
    adaptability = Column(String(10))
    greed = Column(String(10))
    workethic = Column(String(10))
    intelligence = Column(String(10))
    personality = Column(String(10))
    injury = Column(String(10))
    competition = Column(String(10))
    hscol = Column(String(10))
    salary = Column(Integer)
    contractyears = Column(Integer)
    yearsleft = Column(Integer)
    contractvalue = Column(Integer)
    




    def __repr__(self):
        return f'<Player(id={self.id}, name={self.name})>'


