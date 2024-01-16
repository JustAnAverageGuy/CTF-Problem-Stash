# Bank 2 (EASY)

## Description
Can you steal money from the bank and buy the flag?

## Writeup
This is a simple integer overflow challenge, inspired from picoCTF 2019 challenge 'Flag Shop'. The payload requires an input such that 100 times that input turns negative so money can be gained on depositing. As integer overflow starts at 2147483648, one possible payload is 21474837

## FLAG
COPS{l0073d_4g41n}
