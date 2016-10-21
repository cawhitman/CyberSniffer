from unittest import TestCase
from honeypot.models import CyberAttack


class CyberAttackTestCase(TestCase):

    def test_create(self):
        """
        Test creating a new CyberAttack instance.

        :raise AssertionError: If the test fails.
        """
        cyber_attack = CyberAttack(
            source_ip='192.168.56.101', dest_ip='192.168.56.102',
            source_port=22, dest_port=56,
            protocol='6', time=32
        )

        self.assertEqual('192.168.56.101', cyber_attack.source_ip)
        self.assertEqual('192.168.56.102', cyber_attack.dest_ip)
        self.assertEqual(22, cyber_attack.source_port)
        self.assertEqual(56, cyber_attack.dest_port)
        self.assertEqual('6', cyber_attack.protocol)
        self.assertEqual(32, cyber_attack.time)

    def test_repr(self):
        """
        Test the __repr__ method.

        :raise AssertionError: If the test fails.
        """
        cyber_attack = CyberAttack(
            source_ip='192.168.56.101', dest_ip='192.168.56.102',
            source_port=22, dest_port=56,
            protocol='6', time=32
        )

        self.assertEqual("<CyberAttack(source_ip='192.168.56.101', dest_ip='192.168.56.102', "
                         "source_port=22, dest_port=56, protocol='6', time=32)>", repr(cyber_attack))
