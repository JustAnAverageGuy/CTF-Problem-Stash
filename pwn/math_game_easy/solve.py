#! /bin/python3
from pwn import *
import warnings
warnings.filterwarnings('ignore')

target = remote("ctf.copsiitbhu.co.in", 31139)
score = 0

while score < 100:
    target.recvuntil('(')
    s = "(" + target.recvline().decode('utf-8')
    target.recvuntil(':')
    ans = eval(s)
    target.sendline(str(ans))
    score += 1

target.recvuntil("FLAG: ")
print(target.recvline().decode('utf-8'), end="");
