from configs import SESSION
from models import CyberAttack


SESSION.query(CyberAttack).delete()
SESSION.commit()
print(len(SESSION.query(CyberAttack).all()))

cyber_attack = CyberAttack.create(source_ip='127.0.0.1', dest_ip='192.168.56.102',
                                  source_port=22, dest_port=22,
                                  protocol='ssh', time=123456789)
print(len(SESSION.query(CyberAttack).all()))
print(cyber_attack)
