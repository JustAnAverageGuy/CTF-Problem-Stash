# crackme2 (200) - rev

Total solves - 21

Final points - 175

## Description
What are software license keys? Have you ever wondered how they are generated?

`nc ctf.copsiitbhu.co.in 61337`

Author - quinnyx

## Attachment
crackme2

## Writeup
Hex-Rays decompiler in [dogbolt](https://dogbolt.org/?id=0793aa0d-4c58-437c-9f0a-a761dc654fcb) gives

```C
//----- (0000000000401196) ----------------------------------------------------
_BOOL8 __fastcall check_key(int a1)
{
  return 3 * (a1 - 149) % 99 == 0;
}

//----- (00000000004011DF) ----------------------------------------------------
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+0h] [rbp-400h] BYREF
  FILE *stream; // [rsp+8h] [rbp-3F8h]
  char s[1000]; // [rsp+10h] [rbp-3F0h] BYREF
  unsigned __int64 v8; // [rsp+3F8h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  printf("Enter Key: ");
  __isoc99_scanf("%d", &v4);
  if ( check_key(v4) )
  {
    puts("Correct Key! Now Keygen Me.");
    stream = fopen("/flag.txt", "r");
    if ( stream )
    {
      if ( fgets(s, 1000, stream) )
        printf("Here is your flag: %s", s);
      else
        puts("COPS{fake_flag}");
      fclose(stream);
    }
    else
    {
      puts("Error opening flag.txt");
    }
  }
  else
  {
    puts("Wrong Key!");
  }
  return 0;
}
```

> 3 * (a1 - 149) % 99 == 0

There are infinite solutions to this, use any e.g. 182

## FLAG
COPS{l0ck5_4nD_k3y5149}
