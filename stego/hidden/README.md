# hidden (300)

## Description
Look at the picture carefully! It says a lot...

## Writeup
1. `binwalk -e chall.png` - Hint was in the picture
2. `cd _chall.png.extracted`
3. Run this script to automate unzipping
```python
#! /bin/python3

import os

for i in range(2, 100):
    os.system(f"unzip {i}.zip")
    os.system(f"rm {i}.zip")
```
4. `zip2john 100.zip > hashes`
5. `john --wordlist=/home/kn1gh7/wordlists/rockyou.txt hashes`
Password found would be `notfound`

## FLAG
COPS{h1dd3n_w17h_b1nw4lk}
