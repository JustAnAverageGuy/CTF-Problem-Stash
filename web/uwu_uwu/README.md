# uwu_uwu (400) - web

Total solves - 2

Final points - 400

## Description
Okay so for all the anime lovers! This service runs a uwuifier tool to uwuify the passed text. Can you exploit it to find the flag?

http://ctf.copsiitbhu.co.in:41343

Author - kn1gh7

## Attachment
uwuifier.zip

## Writeup
From Dockerfile you can understand that the flag is at `/home/node/app/flag.txt` but you know that /home/node is aliased as `~` which is not filtered in the index.js file.

Thus path traversal works!
Use `~/app/flag.txt`

## FLAG
COPS{this_is_the_longest_flag_in_this_ctf_good_luck_have_fun_decoding_it_hopefully_you_dont_hate_me_end_of_flag}


