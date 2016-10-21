from models import CyberAttack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs import BASE


class DBSession(object):

    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://sensor_dev:mcsc@192.168.56.101/sensor',
                                    echo=True, isolation_level="READ_COMMITTED")
        self.session = sessionmaker(bind=self.engine)()

    def db_connect(self):
        if not self.engine.dialect.has_table(self.engine, CyberAttack):
            BASE.metadata.create_all(bind=self.engine)

        BASE.metadata.reflect(bind=self.engine)

    def db_update(self, cyber_attack):
        self.session.add(cyber_attack)
        self.session.commit()

    def db_clear_attack_table(self):
        self.session.query(CyberAttack).delete()


