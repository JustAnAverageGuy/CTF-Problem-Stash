# ReallyVeryWeirdTIMEforCTF (600) - OSINT

Total solves - 6

Final score - 596

## Description
In our first year, few of us grouped together to create a team called Alpha Nodes and participated in a few CTFs.

We really messed up when we posted a few secret things on our repositories. Can you make sure its not visible anymore?

Author - kn1gh7 & 43h1

## Writeup
When you reach CTFTime, you'll find our [github](https://github.com/pwn-strs) under website in team profile

In this only one repo is different - hackerspace

1. Go to commit history. Commit history with id `cadc446` has the first half of flag - `COPS{7H15_15_7H3_`
2. Under issues, there is 1 closed issue. First comment is edited. If you check the edit history, you'll find [this](https://pastebin.com/9PQ2wMgM) link. The pastebin link has [spam encoded](https://www.spammimic.com/decode.shtml) message that asks about wayback machine. Putting it there shows another spam encoded message which has second half of flag - `F1N4L_B055}`

## FLAG
COPS{7H15_15_7H3_F1N4L_B055}
