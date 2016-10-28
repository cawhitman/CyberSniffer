from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from honeypot.configs import DATABASE, BASE
from honeypot.models import CyberAttack


class Service(object):

    def __init__(self, model, **db_kwargs):
        if db_kwargs['dialect'] == 'postgresql':
            self.engine = create_engine(
                db_kwargs['dialect'] + '+psycopg2://' + db_kwargs['username'] + ':' + db_kwargs['password'] +
                '@' + db_kwargs['host'] + '/' + db_kwargs['database'],
                echo=True, isolation_level="READ_COMMITTED")
        elif db_kwargs['dialect'] == 'sqlite':
            self.engine = create_engine(
                db_kwargs['dialect'] + ':///' + db_kwargs['absolute_path']
            )
        self.session = sessionmaker(bind=self.engine)()
        BASE.metadata.create_all(bind=self.engine)
        self.model = model

    def create_model(self, **kwargs):
        model = self.model(**kwargs)
        self.session.add(model)
        self.session.commit()

        return model

    def clear(self):
        self.session.query(self.model).delete()


class CyberAttackService(Service):

    def __init__(self):
        super().__init__(
            CyberAttack, dialect='postgresql',
            username=DATABASE['USERNAME'], password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'], database=DATABASE['DB_NAME']
        )
