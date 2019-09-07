# coding=utf-8

from py_mysql_binlogserver.lib import Flags
from py_mysql_binlogserver.lib.packet import Packet
from py_mysql_binlogserver.lib.proto import Proto


class Prepare(Packet):
    __slots__ = ('query', ) + Packet.__slots__

    def __init__(self):
        super(Prepare, self).__init__()
        self.query = ''

    def getPayload(self):
        payload = bytearray()

        payload.extend(Proto.build_byte(Flags.COM_STMT_PREPARE))
        payload.extend(Proto.build_eop_str(self.query))

        return payload

    @staticmethod
    def loadFromPacket(packet):
        obj = Prepare()
        proto = Proto(packet, 3)

        obj.sequenceId = proto.get_fixed_int(1)
        proto.get_filler(1)
        obj.query = proto.get_eop_str()

        return obj
