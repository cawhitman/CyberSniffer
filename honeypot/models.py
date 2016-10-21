from sqlalchemy import Column, Integer, String

from honeypot.configs import BASE


class CyberAttack(BASE):
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
