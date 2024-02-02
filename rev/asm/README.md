# asm (1,2,3) (50) - rev

1:

Total solves - 103

Final points - 10

2:

Total solves - 95

Final points - 10

3:

Total solves - 86

Final points - 10

## Description
This challenge is a part of series of 3 challenges (asm 1-3). The purpose is to acquint you with basics of assembly!

This may help a lot - https://www.cs.virginia.edu/~evans/cs216/guides/x86.html

1.
```
xor ax, ax
```
2.
```
mov al, 'd'
mov ah, 0x0d
```
3.
```
.string DB "assembly is cool",0
mov ax, .string
mov si, ax
mov al, [si]
mov ah, 0xd
```

What will be value of ax after this operation in two-byte hex (with 0x) ? 

Flag Format: COPS{answer}

Author - kn1gh7

## Writeup
1. XOR of a value with itself is 0. This will be stored in ax as 0x0000
2. 'd' in hex is 0x64 --> al and 0x0d --> ah. Thus ax is 0x0d64
3. [si] --> 'a', 0x61 --> al, 0x0d --> ah. Thus ax is 0x0d61

## FLAG
1. COPS{0x0000}
2. COPS{0x0d64}
3. COPS{0x0d61}
