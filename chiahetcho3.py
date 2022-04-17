t = int(input())
while t > 0:
    nums = input()
    sum = 0
    for num in range(0, len(nums)):
        sum += int(nums[num])
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1