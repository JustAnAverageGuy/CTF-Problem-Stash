#! /bin/python3
import random

flag = open('/flag.txt').read()
score = 0
max_score = 100
operators = ["+", "-", "*"]
while score < max_score:
    print(f"SCORE: {score}")
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    c = random.randint(0,2)
    s = f"({a}) {operators[c]} ({b})"
    print(s)
    ans = eval(s)
    user = int(input("ANSWER: "))
    if ans == user:
        score += 1
        print("CORRECT!")
        print()
        continue
    else:
        print("WRONG ANSWER!")
        print()
        break;

if score == max_score:
    print(f"NICE! FLAG: {flag}")
