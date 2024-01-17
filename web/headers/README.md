# headers

## Description
Headers? Football?? WHAAAT?

## Writeup
When you go on the website, it says "Not an agent of the C0PS-CTF browser!". So using a tool like burpsuite, change your `User-Agent` to `C0PS-CTF`. Upon visiting the website again, it says "Does not Accept fl4g". So change your `Accept` to `fl4g`. Upon visiting the website again, it says "Connection not s3cur3". So change your `Connection` to `s3cur3`. Upon visiting the website again, it says "Give-Flag is not 7ru3". So add another header, `Give-Flag` and set it to `7ru3`. Upon visiting the website again, you will get the flag!

## FLAG
COPS{7h475_4_g04l!}
