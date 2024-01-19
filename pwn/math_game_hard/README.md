# math game (hard)

## Description
Answer me 10000 times and you get the flag. But there is a catch:

1. Answer each question within 1 second
2. Find both answer and question yourself :D

Can you get it?

## Writeup
```python
#! /bin/python3
from pwn import *
import random
import warnings
warnings.filterwarnings('ignore')

target = remote("ctf.copsiitbhu.co.in", 31140)
# target = process("./math_game.py")
score = 0
random.seed(69696969)
operators = ["+", "-", "*"]
while score < 10000:
    target.recvuntil(':')
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    c = random.randint(0,2)
    s = f"({a}) {operators[c]} ({b})"
    ans = eval(s)
    target.sendline(str(ans))
    score += 1

target.recvuntil("FLAG: ")
print(target.recvline().decode('utf-8'), end="");
```

## FLAG
COPS{m47h5_g0d_0rz}
