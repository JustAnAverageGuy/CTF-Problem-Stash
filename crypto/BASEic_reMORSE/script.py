#!/bin/python3
import re
LETTERS_TO_MC = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}

MC_TO_LETTERS = {i:j for j,i in LETTERS_TO_MC.items()}

def to_morse(message):
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    return " ".join(LETTERS_TO_MC[i] for i in message if i in alphabet)

def from_morse(message:list[str]):
    return "".join(MC_TO_LETTERS[i] for i in message if i in MC_TO_LETTERS)

def convert(morse_code):
    converted = []
    for i in morse_code:
        if i == '.': converted.append('1')
        elif i == '-': converted.append('111')
        else: 
            assert i == ' '
            converted.append('0') # gap between characters is three units
    return "0".join(converted)

def decode(s):
    A = re.split("000", s)
    characters = [ "".join("-" if len(k) == 3 else '.' for k in i.split('0')) for i in A] 
    return characters


if __name__ == "__main__":
    import sys
    message = sys.argv[1]
    print(f'[*] Encoding message={repr(message)}')
    converted = convert(to_morse(message))
    print(f'[!] After encoding: {converted}')
    print(f'[*] Trying to decode')
    recovered = from_morse(decode(converted))
    print(f'[!] Recovered={repr(recovered)}')
    assert recovered == message, "Recovered and message are different"
    from base64 import b64encode
    print(f'[*] Encoding in base64')
    in_hex = hex(int(converted,2))[2:]
    if len(in_hex)%2 == 1: in_hex = '0' + in_hex
    print(f'[!] converted = {b64encode(bytes.fromhex(in_hex)).decode()}')




