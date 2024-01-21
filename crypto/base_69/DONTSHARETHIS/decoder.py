#!/bin/python3

# btw random seed was 420
s = ""
has = 0
encoded = ""

with open("output.txt") as f: exec(f.read())

K = 69
perm = []
t = has
while t>0:
    perm.append(t%K)
    t //= K

N = len(encoded)

invp = [-1]*N
for i,j in enumerate(perm): invp[j] = i

print("".join(encoded[i] for i in invp))

