# CTF-Problem-Stash
Problem Stash for CTFS IIT BHU

`challenge.json` format:
---

```json

{
  "name": "name of the challenge", // name of the challenge
  "category": "pwn", // category of the challeneg
  "author": "kn1gh7", // Author
  "description": "Can you steal money from the bank and buy the flag?", // Description
  "flag": "COPS{l0073d}", // Flag
  "points": 100, // Initial number of points
  "internal_port": 31137, // port to host the challenge on 
  "box": "ctf.copsiitbhu.co.in", // domain to host the challenge on 
  "files": [
    "chall.c" // file attachements for the challenge
  ]
}
```

Add a checkbox with chall category/name so a track of what has been hosted on CTFd can be tracked and we do not miss challs

- [x] misc/impossible
- [x] pwn/bank
- [x] pwn/bank_2  
- [x] OSINT/CoffeeNapCode
- [x] web/admin
- [x] web/comments
- [x] pwn/math_game_easy
- [x] pwn/math_game_hard
- [x] misc/sanity
- [x] misc/survey
- [x] web/headers
- [x] crypto/base69
- [x] crypto/to_be_xor_not_to_be
- [x] pwn/very_easie_pwn
- [x] pwn/easie_pwn
- [x] pwn/executable
- [x] rev/crackme
