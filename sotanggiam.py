# bai nay co cong thuc la s[i-1] va s[i+1]  la cung lon hon s[i] hoac  nho hon nhung chi co 1 lan

t = int(input())

while t > 0:
    number = input()
    count = 0
    for i in range(1, len(number) -1):
        if number[i] == number[i+1]:
            count = 2
        if number[i -1] > number[i] and number[i+1] > number[i]:
            count += 1
        if number[i - 1] < number[i] and number[i + 1] < number[i]:
            count += 1
        if count > 1:
            break
    if len(number) < 3 or count != 1:
        print("NO")
    else:
        print("YES")
    t -= 1