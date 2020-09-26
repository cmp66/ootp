from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory', echo=True)

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    position = Column(String(20))
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
    totalyears = Column(Integer)
    majorleagueyears = Column(Integer)
    majorleaguedays = Column(Integer)
    proyears = Column(Integer)
    draftleague = Column(String)
    draftteam = Column(String)
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
    battedballtype = Column(Integer)
    groundballtype = Column(Integer)
    flyballtype = Column(Integer)
    speedrating = Column(Integer)
    stealrating = Column(Integer)
    baserunningrating = Column(Integer)

    def __repr__(self):
        return f'<PlayerBatting(id={self.id}, name={self.name})>'


class PlayerPitching(Base):
    __tablename__ = 'playerpitching'

    playerid = Column(Integer, primary_key = True)
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
        return f'<PlayerPitching(id={self.id}, name={self.name})>'


class PlayerFielding(Base):
    __tablename__ = 'playerfielding'

    playerid = Column(Integer, primary_key = True)
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
        return f'<PlayerFielding(id={self.id}, name={self.name})>'




