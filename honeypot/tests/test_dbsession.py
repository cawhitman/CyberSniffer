import os
from unittest import TestCase
from honeypot.dbsession import DBSession
from honeypot.models import CyberAttack


class DBSessionTestCase(TestCase):

    def setUp(self):
        """
        Initialize testing data.
        """
        self.db_session = DBSession('sqlite', absolute_path=os.path.dirname(os.path.abspath(__file__)) + '/test_db.db')
        self.cyber_attack = CyberAttack(
            source_ip='192.168.56.101', dest_ip='192.168.56.102',
            source_port=22, dest_port=56,
            protocol='6', time=32
        )
        self.db_session.db_connect()

    def test_connect(self):
        """
        Test the db_connect method.

        :raise AssertionError: If the test fails.
        """
        self.assertListEqual(['CyberAttack'], self.db_session.engine.table_names())

    def test_update(self):
        """
        Test the db_update method.

        :raise AssertionError: If the test fails.
        """
        self.db_session.db_update(self.cyber_attack)
        cyber_attacks = self.db_session.session.query(CyberAttack).all()

        self.assertEqual(1, len(cyber_attacks))
        self.assertEqual(self.cyber_attack, cyber_attacks[0])

    def test_clear(self):
        """
        Test the db_clear_attack_table method.

        :raise AssertionError: If the test fails.
        """
        self.db_session.db_clear_attack_table()
        self.assertEqual(0, len(self.db_session.session.query(CyberAttack).all()))

    def tearDown(self):
        os.remove(os.path.dirname(os.path.abspath(__file__)) + '/test_db.db')