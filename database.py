from datetime import time
from datetime import datetime
import sqlalchemy as db

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
Base = db.orm.declarative_base()

class Reports(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    timeOfReport = Column(String)
    typeOfReport = Column(String)
    stationOfReport = Column(Integer)
    lineOfReport = Column(Integer)
    directionOfLine = Column(String)


class lineStopData(Base):
    __tablename__ = 'lineAndStop'

    id = Column(Integer, primary_key=True)
    stationID = Column(Integer)
    name = Column(String)
    line = Column(String)
    lineSource = Column(String)
    linecompany = Column(String)

    lastKnownArrival = Column(String)

    # problems (max 2 hours)
    error1 = Column(String)  # string is time of last incident, or 0: bus not following line
    error2 = Column(String)  # string is time of last incident: bus missing
    error3 = Column(String)  # string is time of last incident: bus too full, didn't stop
    error4 = Column(String)  # string is time of last incident: bus didn't stop for other reasons

    # long time problems
    problem1 = Column(String)  # string is time of last incident: canceled stop
    problem2 = Column(String)  # string is time of last incident: road work somewhere in line; some stops canceled etc


Base.metadata.create_all(engine)


def addLineStationStop(ID, name, lines, linessource, companies):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = lineStopData(stationID=ID, name=name, lines=lines, linesSource=linessource, linescompany=companies)
    session.add(new_row)
    session.commit()
