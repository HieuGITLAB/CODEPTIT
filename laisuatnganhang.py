t = int(input())
while t > 0:
    key_board = list(input().split())
    fund = float(key_board[0])
    interest = float(key_board[1])/100
    money = float(key_board[2])
    #  A = P * (1+r)^t
    ans = money / fund
    for i in range(1, 100):
        if pow((1+interest), i) - ans > 0:
            print(i)
            break
    t -= 1
