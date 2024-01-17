# math game (easy)

## Description
Answer me 50 times and you get the flag. Easy right?

## Writeup
```python
#! /bin/python3
from pwn import *
import warnings
warnings.filterwarnings('ignore')

target = remote("ctf.copsiitbhu.co.in", 31139)
score = 0

while score < 50:
    target.recvuntil('(')
    s = "(" + target.recvline().decode('utf-8')
    target.recvuntil(':')
    ans = eval(s)
    target.sendline(str(ans))
    score += 1

target.recvuntil("FLAG: ")
print(target.recvline().decode('utf-8'), end="");
```

## FLAG
COPS{m47h5_15_fun}
