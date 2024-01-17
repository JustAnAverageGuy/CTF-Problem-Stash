#! /bin/python3
import random

flag = open('/flag.txt').read()
score = 0
max_score = 10000
operators = ["+", "-", "*"]
random.seed(69696969)
while score < max_score:
    print(f"SCORE: {score}")
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    c = random.randint(0,2)
    s = f"({a}) {operators[c]} ({b})"
    # print(s) yeah try answering now lol
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
