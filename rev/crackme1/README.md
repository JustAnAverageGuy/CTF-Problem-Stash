# crackme 1 (200) - rev

Total solves - 17

Final points - 184

## Description
Find the password for a flag

Author - quinnyx

## Attachment
crackme

## Writeup
ltrace ./crackme , We can see out input is being converted to some string of same length and being compared to some pre defined string which looks somewhat in flag format. Best guess would be caser cipher , brute forcing on decodefr gives us a flag . You can decompile the program to see the encoding function for yourself as well.

## Flag
COPS{iAAmcrACked149}
