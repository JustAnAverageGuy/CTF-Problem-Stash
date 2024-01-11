# Bank (EASY)

## Description
Can you steal money from the bank and buy the flag?

## Writeup
The challenge is inspired from picoCTF 2019 challenge "flag shop".

As signed ints are used, there is scope of integer overflow. Once this is realised any input larger than `2147483649` in deposit would generally give the flag, as its 2's complement notation is negative, and substracting it would give a positive number in money.

## FLAG
COPS{1n7_0v3rfl0w_70_r35cu3}