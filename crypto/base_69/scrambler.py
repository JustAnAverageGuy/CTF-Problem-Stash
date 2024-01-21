#!/bin/python3

from random import shuffle

FLAG = "SECRET"
N = len(FLAG)

perm = [*range(N)]
shuffle(perm)


scrambled = "".join(FLAG[i] for i in perm)

has = 0
t = 1

for i in perm:
    has += i * t
    t   *= 69

with open("output.txt", "w") as f: print(f'{has=}\n{scrambled=}',file=f)
