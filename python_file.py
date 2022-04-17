name = input().lower()
length = len(name)
def check(name):
    if len(name) < 3:
        return False
    if name[length-1].lower() != "y" or name[length-2].lower() != "p" or name[length -3] != ".":
        return False
    check = 0
    for i in range(0, length- 4):
        if (name[i] >= "a" and name[i] <= "z") or name[i] == "_":
             check = 0
        else:
            return False
    if check == 1:
        return False
    return True

if check(name) == True:
    print("yes")
else:
    print("no")


