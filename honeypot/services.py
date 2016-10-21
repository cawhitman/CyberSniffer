from honeypot.configs import DATABASE
from honeypot.dbsession import DBSession
from honeypot.models import CyberAttack


class Service(object):

    def __init__(self, model):
        self.db_session = DBSession(dialect='postgresql', username=DATABASE['USERNAME'], password=DATABASE['PASSWORD'],
                                    host=DATABASE['HOST'], database=DATABASE['DB_NAME'])
        self.db_session.db_connect()
        self.model = model

    def create_model(self, **kwargs):
        model = self.model(**kwargs)
        self.db_session.db_update(model)

        return model


class CyberAttackService(Service):

    def __init__(self):
        super().__init__(CyberAttack)
