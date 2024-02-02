# do you know RSA (100) - crypto

Total solves - 48

Final score - 30

## Description
Just checking whether you know about RSA

Author - nirvana

## Attachment
script.py

output.txt

## Writeup
```python
from Crypto.Util.number import *
e =  0x10001
with open("./output.txt") as f: exec(f.read())
d = pow(e, -1, (p-1)*(q-1))
n = p*q
print(long_to_bytes(pow(c, d, n)))

# flag = COPS{n1c3_50_y0u_d0_kn0w_R5A}
```

## FLAG
COPS{n1c3_50_y0u_d0_kn0w_R5A}