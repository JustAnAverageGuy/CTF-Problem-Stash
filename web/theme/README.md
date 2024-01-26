# theme (300)

## Description
I made a simple app that can give the binary representation of a number. Well the main feature is theme switcher! I have added two themes for now but I want to make sure its safe. Can you help me?

http://ctf.copsiitbhu.co.in:41342/

Author - kn1gh7

## Attachment
Dockerfile
server.py

## Writeup
Path traversal is possible in theme argument. Do `?theme=../flag.txt`

## FLAG
COPS{s1mpl3_p4th_7r4v3r53l}

