#!/bin/python3

s = bytes.fromhex("68647b78506443070b5f434a5f0b7364790b5c4a580b45445f0b4a0b5f525b4456")
to_be = 0x2B

print(bytes([i^to_be for i in s]).decode())
