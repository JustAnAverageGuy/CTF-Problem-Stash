from Crypto.Util.number import *
e =  0x10001

n = -1
c = -1
cheat = -1

with open("./output.txt") as f: exec(f.read())

# cheat == p + q
# n == p*q

B = -cheat
C = n

from math import isqrt
D = B*B - 4 * C
D = isqrt(D)

p = (-B + D)//2
q = (-B - D)//2


d = pow(e, -1, (p-1)*(q-1))
n = p*q
print(long_to_bytes(pow(c, d, n)))

# flag = COPS{n1c3_50_y0u_4c7u411y_d0_kn0w_R5A}
