#! /bin/python3

flag = open('/flag.txt').read()

while True:
    s = input("Enter the string: ")
    if len(s) >= 20:
        print("String too long!!")
        print()
    elif len(s.upper()) < 25:
        print("String too short!!")
        print()
    elif len(s.upper()) > 25:
        print("String too long!!")
        print()
    else:
        print(f"Well done! FLAG: {flag}")
        break
