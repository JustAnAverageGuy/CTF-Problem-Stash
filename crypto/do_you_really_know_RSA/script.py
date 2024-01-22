from Crypto.Util.number import getPrime

FLAG = b'COPS{definitely_real_flag}'

p,q = getPrime(1024), getPrime(1024)
# print(f'{p=}\n{q=}') # not this time

m = int((FLAG).hex(), 16)
e = 0x10001
n = p*q

c = pow(m, e, n)
n = p*q
cheat = (pow(p,q,n) + pow(q,p,n))%n
print(f"n = 0x{n:x}")
print(f"c = 0x{c:x}")
print(f"cheat = 0x{cheat:x}")

