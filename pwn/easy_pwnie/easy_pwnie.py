#! /bin/python3

try:
    ans = eval(input("Do you want the flag? "))
    print(f"You entered {ans}")
    if ans == "yes":
        print("Yay! You want that flag!")
        quit()
except:
    pass

print('sed :(')
    
