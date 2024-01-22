#!/bin/python3

from collections import defaultdict
from itertools   import product
from hashlib     import md5

hash = "0bac031947cd7251ae25f4cf7f2a78b7"
alphabet = b'COPS{}abcdefghijklmnopqrstuvwxyz0123456789_'

p = 49999

ratios = [24051, 40964, 38430, 30804, 35268, 43879, 4904, 4211, 6252, 11010, 33655, 47549, 34314, 4001, 38000]

invratios = defaultdict(list)

for i,j in product(alphabet, repeat=2):
    k = i * pow(j, -1,p)%p
    if k in ratios: invratios[k].append(f'{chr(i)}{chr(j)}')

possiblities = [""]

for i in ratios:
    new_possiblities = []
    for x in invratios[i]:
        for j, k in enumerate(possiblities):
            new_possiblities.append(k + x)

    possiblities = new_possiblities[::]
    new_possiblities = []


for i in possiblities:
    if hash == md5(i.encode()).digest().hex(): print(i)

# flag = COPS{yup_pr1m35_f0rm_4_f13ld_}
