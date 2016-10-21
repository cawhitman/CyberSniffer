from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///honeypot_db.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class CyberAttack(Base):
    __tablename__ = 'CyberAttack'

    id = Column(Integer, primary_key=True)
    source_ip = Column(String(80))
    dest_ip = Column(String(80))
    source_port = Column(Integer)
    dest_port = Column(Integer)
    protocol = Column(String(80))
    time = Column(Integer)

    def __repr__(self):
        return "<CyberAttack(" \
               "source_ip='{0}', dest_ip='{1}', " \
               "source_port={2}, dest_port={3}, " \
               "protocol='{4}', time={5}" \
               ")>".format(self.source_ip, self.dest_ip, self.source_port, self.dest_port, self.protocol, self.time)

Base.metadata.reflect(bind=engine)
session.query(CyberAttack).delete()
session.commit()

cyber_attack = CyberAttack(source_ip='127.0.0.1', dest_ip='192.168.56.102',
                           source_port=22, dest_port=22,
                           protocol='ssh', time=123456789)
session.add(cyber_attack)
session.commit()
print(len(session.query(CyberAttack).all()))