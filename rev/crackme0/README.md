# crackme 0 (100) - rev

Total solves - 17

Final points - 184

## Description
Enter the flag. But first find it lol

Author - kn1gh7

## Attachment
crackme0

## Writeup
`strings crackme | grep COPS` gives COPS{pl41nt3xt_fl4g}

Hex-Rays decompiler in [dogbolt](https://dogbolt.org/?id=c9fd9ca1-c890-4bda-ada1-1dcfe1762512) gives

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char *s; // [rsp+8h] [rbp-8h]

  setbuf(stdout, 0LL);
  while ( 1 )
  {
    printf("Enter flag > ");
    fgets(s, 100, stdin);
    if ( !strcmp(s, "COPS{pl41nt3xt_fl4g}\n") )
      break;
    puts("You lose! Try again!");
  }
  puts("Congratulations! You got the flag!");
  return 0;
}
```
Can be seen from here also

## FLAG
COPS{pl41nt3xt_fl4g}
