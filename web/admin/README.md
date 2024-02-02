# admin (200) - web

Total solves - 72

Final points - 40

## Description
Can you login as admin into the website that I made?

http://ctf.copsiitbhu.co.in:41338

Author - quinnyx

## Writeup
The webpage dosen't actually send any request to server when we click login.
So on checking index.js we can see our inputs are being converted to base64 then to rot13(by the function encode).
Reversing the operations on the predefined password gives us a flag.

## Flag
COPS{09r0T13c1ph3r14}
