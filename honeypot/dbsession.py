from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from honeypot.configs import BASE
from honeypot.models import CyberAttack


class DBSession(object):

    def __init__(self, dialect, **kwargs):
        if dialect == 'postgresql':
            self.engine = create_engine(
                dialect + '+psycopg2://' + kwargs['username'] + ':' + kwargs['password'] +
                '@' + kwargs['host'] + '/' + kwargs['database'],
                echo=True, isolation_level="READ_COMMITTED")
        elif dialect == 'sqlite':
            self.engine = create_engine(
                dialect + ':///' + kwargs['absolute_path']
            )
        self.session = sessionmaker(bind=self.engine)()

    def db_connect(self):
        BASE.metadata.create_all(bind=self.engine)

    def db_update(self, cyber_attack):
        self.session.add(cyber_attack)
        self.session.commit()

    def db_clear_attack_table(self):
        self.session.query(CyberAttack).delete()


