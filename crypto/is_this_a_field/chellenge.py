#!/bin/python3

from hashlib import md5

flag = b"SECRET"

assert all(i in b'COPS{}abcdefghijklmnopqrstuvwxyz0123456789_' for i in flag)
assert len(flag)%2 == 0
hash = md5(flag).hexdigest()

x = 49999
ratios = []

for k in range(len(flag) // 2):
    i = flag[2*k]
    j = flag[2*k + 1]
    ratios.append(i * pow(j,-1,x) % x)

print(f'ratios = {ratios}')
print(f'hash = {hash}')

## output ##

# ratios = [24051, 40964, 38430, 30804, 35268, 43879, 4904, 4211, 6252, 11010, 33655, 47549, 34314, 4001, 38000]
# hash = 0bac031947cd7251ae25f4cf7f2a78b7
