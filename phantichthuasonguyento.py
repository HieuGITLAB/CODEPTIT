t = int(input())

while t > 0:
    num = int(input())
    s= "1 * "
    for i in range(2, 100):
        count = 0
        flag = False
        while num % i == 0:
            count += 1
            flag = True
            num /= i
            num = int(num)
        if flag and num != 1:
            s += str(i) +"^"+ str(count) +" * "
        if flag and num == 1:
            s += str(i) + "^" + str(count)
    if num != 1:
        s += str(num) +"^" +  "1"
    print(s,sep=" ")
    t -= 1