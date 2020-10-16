from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    timestamp = Column(Date, primary_key = True)
    position = Column(String(20))
    name = Column(String(64))
    team = Column(String(32))
    org = Column(String(32))
    league = Column(String(32))
    level = Column(String(32))
    dob = Column(Date)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    bats = Column(String(32))
    throws = Column(String(32))
    leader = Column(String(32))
    loyalty = Column(String(32))
    adaptability = Column(String(32))
    greed = Column(String(32))
    workethic = Column(String(32))
    intelligence = Column(String(32))
    personality = Column(String(32))
    injury = Column(String(32))
    competition = Column(String(32))
    hscol = Column(String(32))
    salary = Column(Integer)
    contractyears = Column(Integer)
    yearsleft = Column(Integer)
    contractvalue = Column(Integer)
    totalyears = Column(Integer)
    majorleagueyears = Column(Integer)
    majorleaguedays = Column(Integer)
    proyears = Column(Integer)
    draftleague = Column(String(32))
    draftteam = Column(String(32))
    draftyear = Column(Integer)
    draftround = Column(Integer)
    draftsupplimental = Column(Integer)
    draftpick = Column(Integer)
    overallpick= Column(Integer)
    discoveryyear = Column(Integer)
    discoveryteam = Column(String(32))

    def __repr__(self):
        return f'<Player(id={self.id}, name={self.name})>'

class PlayerBatting(Base):
    __tablename__ = "playerbatting"

    playerid = Column(Integer, primary_key = True)
    timestamp = Column(Date, primary_key = True)
    name = Column(String(64))
    contactrating = Column(Integer)
    gaprating = Column(Integer)
    powerrating = Column(Integer)
    eyerating = Column(Integer)
    krating = Column(Integer)
    contactvleft = Column(Integer)
    gapvleft = Column(Integer)
    powervleft = Column(Integer)
    eyevleft = Column(Integer)
    kvleft = Column(Integer)
    contactvright = Column(Integer)
    gapvright = Column(Integer)
    powervright = Column(Integer)
    eyevright = Column(Integer)
    kvright = Column(Integer)
    contactpotential = Column(Integer)
    gappotential = Column(Integer)
    powerpotential = Column(Integer)
    eyeprotential = Column(Integer)
    kprotential = Column(Integer)
    buntrating = Column(Integer)
    buntforhitrating = Column(Integer)
    battedballtype = Column(String(32))
    groundballtype = Column(String(32))
    flyballtype = Column(String(32))
    speedrating = Column(Integer)
    stealrating = Column(Integer)
    baserunningrating = Column(Integer)

    def __repr__(self):
        return f'<PlayerBatting(id={self.playerid}, name={self.name})>'


class PlayerPitching(Base):
    __tablename__ = 'playerpitching'

    playerid = Column(Integer, primary_key = True)
    timestamp = Column(Date, primary_key = True)
    name = Column(String(64))
    team = Column(String(64))
    stuffrating = Column(Integer)
    movementrating = Column(Integer)
    controlrating = Column(Integer)
    stuffvleft = Column(Integer)
    movementvleft = Column(Integer)
    controlvleft = Column(Integer)
    stuffvright = Column(Integer)
    movementvright = Column(Integer)
    controlvright = Column(Integer)
    stuffpotential = Column(Integer)
    movementpotential = Column(Integer)
    controlpotential = Column(Integer)
    fastballrating = Column(Integer)
    fastballpotential = Column(Integer)
    changeuprating = Column(Integer)
    changeuppotential = Column(Integer)
    curveballrating = Column(Integer)
    curveballpotential = Column(Integer)
    sliderrating = Column(Integer)
    sliderpotential = Column(Integer)
    sinkerrating = Column(Integer)
    sinkerpotential = Column(Integer)
    splitterrating = Column(Integer)
    splitterpotential = Column(Integer)
    cutterrating = Column(Integer)
    cutterpotential = Column(Integer)
    forkballrating = Column(Integer)
    forkballpotential = Column(Integer)
    circlechangerating = Column(Integer)
    circlechangepotential = Column(Integer)
    screwballrating = Column(Integer)
    screwballpotential = Column(Integer)
    knucklecurverating = Column(Integer)
    knucklecurvepotential = Column(Integer)
    knuckleballrating = Column(Integer)
    knuckleballpotential = Column(Integer)
    numpitches = Column(Integer)
    groundballflyball = Column(String(16))
    velocity = Column(Integer)
    armslot = Column(String(16))
    pitchertype = Column(String(16))
    stamina = Column(Integer)

    def __repr__(self):
        return f'<PlayerPitching(id={self.playerid}, name={self.name})>'


class PlayerFielding(Base):
    __tablename__ = 'playerfielding'

    playerid = Column(Integer, primary_key = True)
    timestamp = Column(Date, primary_key = True)
    name = Column(String(64))
    team = Column(String(64))
    infieldrange = Column(Integer)
    infieldarm = Column(Integer)
    turndoubleplay = Column(Integer)
    infielderror = Column(Integer)
    outfieldrange = Column(Integer)
    outfieldarm = Column(Integer)
    outfielderror = Column(Integer)
    catcherarm = Column(Integer)
    catcherability = Column(Integer)
    priamrydefensiverating = Column(Integer)
    pitcherrating = Column(Integer)
    catcherrating = Column(Integer)
    firstbaserating = Column(Integer)
    secondbaserating = Column(Integer)
    thirdbaserating = Column(Integer)
    shortstoprating = Column(Integer)
    leftfieldrating = Column(Integer)
    centerfieldrating = Column(Integer)
    rightfieldrating = Column(Integer)

    def __repr__(self):
        return f'<PlayerFielding(id={self.playerid}, name={self.name})>'

class OOTPDbAccess():

    def __init__(self, type, host, user, password):   
        if type == 'mysql':
            print(f'Creating mysql db connection to {host}')
            self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:3306/ootp',
    echo=True)
            Base.metadata.create_all(self.engine)
        else:
            print('Creating sqllite connnection')
            self.engine = create_engine('sqlite:///:memory', echo=True)
        Session  = sessionmaker(bind=self.engine)
        self.session = Session()


    def add_player_record(self, player_record):
        existing_user = self.session.query(Player).filter_by(id=player_record.id).filter_by(timestamp=player_record.timestamp).first()
        if existing_user is None:
            print(f'adding player {player_record.name}')
            self.session.add(player_record)
            self.session.commit()

    def add_player_batting_record(self, player_batting_record):
        existing_user = self.session.query(PlayerBatting).filter_by(playerid=player_batting_record.playerid).filter_by(timestamp=player_batting_record.timestamp).first()
        if existing_user is None:
            print(f'adding batting record for player {player_batting_record.name}')
            self.session.add(player_batting_record)
            self.session.commit()

    def add_player_fielding_record(self, player_fielding_record):
        existing_user = self.session.query(PlayerFielding).filter_by(playerid=player_fielding_record.playerid).filter_by(timestamp=player_fielding_record.timestamp).first()
        if existing_user is None:
            print(f'adding fielding record for player {player_fielding_record.name}')
            self.session.add(player_fielding_record)
            self.session.commit()

    def add_player_pitching_record(self, player_pitching_record):
        existing_user = self.session.query(PlayerPitching).filter_by(playerid=player_pitching_record.playerid).filter_by(timestamp=player_pitching_record.timestamp).first()
        if existing_user is None:
            print(f'adding pitching record for player {player_pitching_record.name}')
            self.session.add(player_pitching_record)
            self.session.commit()




