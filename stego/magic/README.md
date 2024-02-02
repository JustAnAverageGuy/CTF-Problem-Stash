# magic (400) - stego

Total solves - 5

Final points - 398

## Description
Hiding stuff in images is like magic right? Well lets see if you can break this magic.

Remember - Jo dikhta h vo hota nhi aur jo hota a vo dikhta nhi

Author - kn1gh7

## Attachment
chall.png

## Writeup
First fix the header - `FF D8 FF E0 00 10 4A 46 49 46 00 01` (hint was in title - these are called **magic** bytes)

Then increase the height using hex values. Change `ff c0 00 11 08 00 a8 01 c2` with `ff c0 00 11 08 00 c8 01 c2` (hint was in description - Jo dikhta h vo hota nhi aur **jo hota a vo dikhta nhi**)

![flag](org.jpg)

## FLAG
COPS{h1dd3n_fl4g}
