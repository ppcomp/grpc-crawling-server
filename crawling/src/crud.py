from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from crawling.src.entity import Notice
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()
Base = declarative_base()

#create a table we call the create_all with the engine
Base.metadata.create_all(engine)

#destroy this table (and all tables) in the database
# Base.metadata.drop_all(engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

notice = Notice.Notice(
    id="test",
    site = "test",
    title = "test",
    link = "test"
)

s.add(notice)
s.commit()

print(s.query(Notice.Notice).all())