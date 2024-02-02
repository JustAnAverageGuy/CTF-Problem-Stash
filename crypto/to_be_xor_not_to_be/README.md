# to be xor not to be (100) - crypto

Total solves - 83

Final score - 20

## Description
> To be, xor not to be, that is the question

Anyways here's the encoded stuff:
```
68647b78506443070b5f434a5f0b7364790b5c4a580b45445f0b4a0b5f525b4456
```
Author - nirvana

## Writeup
```python
#!/bin/python3

s = bytes.fromhex("68647b78506443070b5f434a5f0b7364790b5c4a580b45445f0b4a0b5f525b4456")
to_be = 0x2B

print(bytes([i^to_be for i in s]).decode())
```

## FLAG
COPS{Oh, that XOR was not a typo}