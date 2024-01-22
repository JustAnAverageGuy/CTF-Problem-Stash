from Crypto.Util.number import *

FLAG = b'COPS{fake_flag}'

p,q = getPrime(1024), getPrime(1024)
print(f'{p=}\n{q=}')

m = bytes_to_long(FLAG)
e = 0x10001
n = p*q

c = pow(m, e, n)
print("c=",hex(c))

