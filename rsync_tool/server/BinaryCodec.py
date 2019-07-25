#!/usr/bin/env python3

import json

class BinaryCodec:
    def __init__(self):
        pass

    def encode(self, obj):
        assert not isinstance(obj, bytes)
        jstr = json.dumps(obj)
        byte = bytes(jstr,'utf-8')
        return byte

    def decode(self, byte):
        assert isinstance(byte,bytes)
        jstr = byte.decode()
        obj = json.loads(jstr)
        return obj

bc = BinaryCodec()
d = { '1':'one','2':'two','3':'three' }

byte = bc.encode(d)
print(byte, type(byte))

od = bc.decode(byte)
print(od,type(od))
print(od['1'])
