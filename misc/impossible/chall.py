#! /bin/python3

flag = open('/flag.txt').read()

s = input("Enter the string: ")

if len(s) >= 20:
    print("String too long!!")
elif len(s.upper()) < 25:
    print("String too short!!")
elif len(s.upper()) > 25:
    print("String too long!!")
else:
    print(f"Well done! FLAG: {flag}")
