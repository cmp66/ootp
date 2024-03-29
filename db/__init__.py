from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.exc import IntegrityError, InvalidRequestError
import os
import datetime

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    default_date = datetime.datetime.strptime("01/01/1900", "%m/%d/%Y")

    id = Column(Integer, primary_key=True)
    timestamp = Column(Date, primary_key=True)
    position = Column(String(20))
    name = Column(String(128))
    team = Column(String(32), default='')
    org = Column(String(32), default='')
    league = Column(String(32), default='')
    level = Column(String(32), default='')
    dob = Column(Date, default=default_date)
    age = Column(Integer, default=0)
    height = Column(Integer, default=0)
    weight = Column(Integer, default=0)
    bats = Column(String(32))
    overall = Column(Integer)
    potential = Column(Integer)
    throws = Column(String(32))
    leader = Column(String(32), default="")
    loyalty = Column(String(32), default="")
    adaptability = Column(String(32), default="")
    greed = Column(String(32), default="")
    workethic = Column(String(32), default="")
    intelligence = Column(String(32), default="")
    personality = Column(String(32), default="")
    injury = Column(String(32), default="")
    competition = Column(String(32), default="")
    hscol = Column(String(32), default="")
    salary = Column(Integer, default=0)
    contractyears = Column(Integer, default=0)
    yearsleft = Column(Integer, default=0)
    contractvalue = Column(Integer, default=0)
    totalyears = Column(Integer, default=0)
    majorleagueyears = Column(Integer, default=0)
    majorleaguedays = Column(Integer, default=0)
    proyears = Column(Integer, default=0)
    draftleague = Column(String(32), default="")
    draftteam = Column(String(32),default="")
    draftyear = Column(Integer, default=0)
    draftround = Column(Integer, default=0)
    draftsupplimental = Column(Integer, default=0)
    draftpick = Column(Integer, default=0)
    overallpick = Column(Integer, default=0)
    discoveryyear = Column(Integer, default=0)
    discoveryteam = Column(String(32), default="")

    def __repr__(self):
        return f"<Player(id={self.id}, name={self.name})>"


class PlayerBatting(Base):
    __tablename__ = "playerbatting"

    playerid = Column(Integer, ForeignKey("players.id"), primary_key=True)
    timestamp = Column(Date, primary_key=True)
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
    babipoverall = Column(Integer)
    babippotential = Column(Integer)

    def __repr__(self):
        return f"<PlayerBatting(id={self.playerid}, name={self.name})>"


class PlayerPitching(Base):
    __tablename__ = "playerpitching"

    playerid = Column(Integer, ForeignKey("players.id"), primary_key=True)
    timestamp = Column(Date, primary_key=True)
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
        return f"<PlayerPitching(id={self.playerid}, name={self.name})>"


class PlayerFielding(Base):
    __tablename__ = "playerfielding"

    playerid = Column(Integer, ForeignKey("players.id"), primary_key=True)
    timestamp = Column(Date, primary_key=True)
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
        return f"<PlayerFielding(id={self.playerid}, name={self.name})>"


class PlayerStats(Base):
    __tablename__ = "playerstats"

    playerid = Column(Integer, ForeignKey("players.id"), primary_key=True)
    season = Column(Integer, primary_key=True)
    position = Column(String(32))
    name = Column(String(64))
    plateapp = Column(Integer)
    battingwar = Column(Float)
    ip = Column(Float)
    battersfaced = Column(Float)
    pitchingwar = Column(Float)
    zonerating = Column(Float)
    defeff = Column(Float)
    woba = Column(Float)
    wrcplus = Column(Float)
    babip = Column(Float)
    kminuswalk = Column(Float)
    fip = Column(Float)
    opsplus = Column(Float)
    whip = Column(Float)


class PlayerReports(Base):
    __tablename__ = "playerreport"

    playerid = Column(Integer, ForeignKey("players.id"), primary_key=True)
    timestamp = Column(Date, primary_key=True)
    position = Column(String(32))
    team = Column(String(32))
    current = Column(Float, default=0.0)
    potential = Column(Float, default=0.0)
    pitcherratingsdiffcurrent = Column(Integer, default=0)
    pitcherratingsdiffpotential = Column(Integer, default=0)
    batterratingsdiffcurrent = Column(Integer, default=0)
    batterratingsdiffpotential = Column(Integer, default=0)
    starteroverallpotential = Column(Integer, default=0)
    starterbasepotential = Column(Integer, default=0)
    starterindivpotential = Column(Integer, default=0)
    starteroverallcurrent = Column(Integer, default=0)
    starterbasecurrent = Column(Integer, default=0)
    starterindivcurrent = Column(Integer, default=0)
    reliefoverallpotential = Column(Integer)
    reliefbasepotential = Column(Integer)
    reliefindivpotential = Column(Integer)
    reliefoverallcurrent = Column(Integer, default=0)
    reliefbasecurrent = Column(Integer, default=0)
    reliefindivcurrent = Column(Integer, default=0)
    batteroverallpotential = Column(Integer, default=0)
    batteroverallbattingpotential = Column(Integer, default=0)
    batteroverallfieldingpotential = Column(Integer, default=0)
    batteroverallcurrent = Column(Integer, default=0)
    batteroverallbattingcurrent = Column(Integer, default=0)
    batteroverallfieldingcurrent = Column(Integer, default=0)
    starteroverallvLeft = Column(Integer, default=0)
    starterbasevLeft = Column(Integer, default=0)
    starteroverallvRight = Column(Integer, default=0)
    starterbasevRight = Column(Integer, default=0)
    relieveroverallvLeft = Column(Integer, default=0)
    relieverbasevLeft = Column(Integer, default=0)
    relieveroverallvRight = Column(Integer, default=0)
    relieverbasevRight = Column(Integer, default=0)
    batteroverallvLeft = Column(Integer, default=0)
    batterbattingvLeft = Column(Integer, default=0)
    batteroverallvRight = Column(Integer, default=0)
    batterbattingvRight = Column(Integer, default=0)
    catcheroverall = Column(Integer, default=0)
    firstbaseoverall = Column(Integer, default=0)
    secondbaseoverall = Column(Integer, default=0)
    thirdbaseoverall = Column(Integer, default=0)
    shortstopoverall = Column(Integer, default=0)
    leftfieldoverall = Column(Integer, default=0)
    centerfieldoverall = Column(Integer, default=0)
    rightfieldoverall = Column(Integer, default=0)
    
class OOTPDbAccess:
    def __init__(self, save_name):
        type = os.environ["DB_TYPE"]
        host = os.environ["DB_HOST"]
        user = os.environ["DB_USERNAME"]
        password = os.environ["DB_PASSWORD"]
        if type == "mysql":
            self.engine = create_engine(
                f"mysql+pymysql://{user}:{password}@{host}:3306/{save_name}", echo=False
            )
            Base.metadata.create_all(self.engine)
        else:
            self.engine = create_engine("sqlite:///:memory", echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_session(self):
        return self.session

    def _update_existing_player(self, existing_player, new_player):
        pass

    def add_player_record(self, player_record):
        existing_player = (
            self.session.query(Player)
            .filter_by(id=player_record.id)
            .filter_by(timestamp=player_record.timestamp)
            .first()
        )
        if existing_player is None:
            print(f"adding player {player_record.name}")
            self.session.add(player_record)
        else:
            self._update_existing_player(existing_player, player_record)

        self.session.commit()

    def add_player_batting_record(self, player_batting_record):
        existing_user = (
            self.session.query(PlayerBatting)
            .filter_by(playerid=player_batting_record.playerid)
            .filter_by(timestamp=player_batting_record.timestamp)
            .first()
        )
        if existing_user is None:
            print(f"adding batting record for player {player_batting_record.name}")
            self.session.add(player_batting_record)
            self.session.commit()
        
    def update_player_batting_record(self, player_batting_record):
        print(f"updating batting record for player {player_batting_record.name}")
        self.session.add(player_batting_record)
        self.session.commit()


    def add_player_fielding_record(self, player_fielding_record):
        existing_user = (
            self.session.query(PlayerFielding)
            .filter_by(playerid=player_fielding_record.playerid)
            .filter_by(timestamp=player_fielding_record.timestamp)
            .first()
        )
        if existing_user is None:
            print(f"adding fielding record for player {player_fielding_record.name}")
            self.session.add(player_fielding_record)
            self.session.commit()

    def add_player_pitching_record(self, player_pitching_record):
        existing_user = (
            self.session.query(PlayerPitching)
            .filter_by(playerid=player_pitching_record.playerid)
            .filter_by(timestamp=player_pitching_record.timestamp)
            .first()
        )
        if existing_user is None:
            print(f"adding pitching record for player {player_pitching_record.name}")
            self.session.add(player_pitching_record)
            self.session.commit()

    def add_player_stats_record(self, player_stats_record):
        existing_user = (
            self.session.query(Player)
            .filter_by(id=player_stats_record.playerid)
            .first()
        )
        if existing_user is None:
            return
        existing_record = (
            self.session.query(PlayerStats)
            .filter_by(playerid=player_stats_record.playerid)
            .filter_by(season=player_stats_record.season)
            .first()
        )
        if existing_record is None:
            print(f"adding stats record for player {player_stats_record.name}")
            self.session.add(player_stats_record)
            try:
                self.session.commit()
            except IntegrityError:
                print("Integrity Error")
                return
            except InvalidRequestError:
                print("InvalidRequestError Error")
                return

    def add_player_report_record(self, player_report_record):
        existing_report = (
            self.session.query(PlayerReports)
            .filter_by(playerid=player_report_record.playerid)
            .filter_by(timestamp=player_report_record.timestamp)
            .first()
        )
        if existing_report is None:
            self.session.add(player_report_record)
            try:
                self.session.commit()
            except IntegrityError:
                print("Integrity Error")
                return
            except InvalidRequestError:
                print("InvalidRequestError Error")
                return

    def get_stats_by_season(self, season):
        return (
            self.session.query(PlayerStats)
            .filter(PlayerStats.season == season)
            .limit(10000)
        )

    def get_player_by_id(self, id):
        return self.session.query(Player).filter(Player.id == id).first()

    def get_player_by_date(self, id, import_date):
        return (
            self.session.query(Player)
            .filter(Player.id == id)
            .filter(Player.timestamp == import_date)
            .first()
        )

    def get_batting_record(self, id, timestamp):
        return (
            self.session.query(PlayerBatting)
            .filter(PlayerBatting.playerid == id)
            .filter(PlayerBatting.timestamp == timestamp)
            .first()\
        )

    def get_pitching_record(self, id, timestamp):
        return (
            self.session.query(PlayerPitching)
            .filter(PlayerPitching.playerid == id)
            .filter(PlayerPitching.timestamp == timestamp)
            .first()
        )
        
    def get_fielding_record(self, id, timestamp):
        return (
            self.session.query(PlayerFielding)
            .filter(PlayerFielding.playerid == id)
            .filter(PlayerFielding.timestamp == timestamp)
            .first()
        )

    def get_player_report(self, id, timestamp):
         return (
            self.session.query(PlayerReports)
            .filter(PlayerReports.playerid == id)
            .filter(PlayerReports.timestamp == timestamp)
            .first()
        )

    def get_player_stats(self, id, season):
         return (
            self.session.query(PlayerStats)
            .filter(PlayerStats.playerid == id)
            .filter(PlayerStats.season == season)
            .first()
        )

    def get_all_players_by_date(self, import_date):
        return self.session.query(Player).filter(Player.timestamp == import_date)

    def get_all_players(self):
        return self.session.query(Player)

    def get_all_batting_records_by_date(self, timestamp):
        return self.session.query(PlayerBatting).filter(PlayerBatting.timestamp == timestamp)

    def get_all_timestamps(self):
        timestamps = self.session.query(PlayerBatting.timestamp).group_by(PlayerBatting.timestamp).all()
        return [value for value, in timestamps]


    def get_all_mlb_players_by_date(self, import_date):
        return (
            self.session.query(Player)
            .filter(Player.timestamp == import_date)
            .filter(Player.level == 'MLB')
        )
