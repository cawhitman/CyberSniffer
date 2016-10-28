import os
from unittest import TestCase
from honeypot.services import Service
from honeypot.models import CyberAttack


class ServiceTestCase(TestCase):

    def setUp(self):
        """
        Initialize testing data.
        """
        self.service = Service(CyberAttack, dialect='sqlite',
                               absolute_path=os.path.dirname(os.path.abspath(__file__)) + '/test_db.db')
        self.cyber_attack = CyberAttack(
            source_ip='192.168.56.101', dest_ip='192.168.56.102',
            source_port=22, dest_port=56,
            protocol='6', time=32
        )

    def test_init(self):
        """
        Test the init method.

        :raise AssertionError: If the test fails.
        """
        self.assertListEqual(['CyberAttack'], self.service.engine.table_names())

    def create_model(self):
        """
        Test the create_model method.

        :raise AssertionError: If the test fails.
        """
        self.service.create_model(
            source_ip='192.168.56.101', dest_ip='192.168.56.102',
            source_port=22, dest_port=56,
            protocol='6', time=32
        )
        cyber_attacks = self.service.session.query(CyberAttack).all()

        self.assertEqual(1, len(cyber_attacks))
        self.assertEqual(repr(self.cyber_attack), repr(cyber_attacks[0]))

    def test_clear(self):
        """
        Test the db_clear_attack_table method.

        :raise AssertionError: If the test fails.
        """
        self.service.session.add(self.cyber_attack)
        self.service.session.commit()
        self.service.clear()
        self.assertEqual(0, len(self.service.session.query(CyberAttack).all()))

    def tearDown(self):
        os.remove(os.path.dirname(os.path.abspath(__file__)) + '/test_db.db')
