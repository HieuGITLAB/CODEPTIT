sentence = list(input())
length = len(sentence)
comma = 0
if length % 3 == 0:
    comma = length / 3 - 1
else:
    comma = int(length/3)
distance = -3
for i in range(length - 1, 0, -1):
    if comma == 0:
        break
    elif i != 0 and i :
        sentence.insert(distance, ",")
        comma -= 1
        distance -= 4
print(*sentence, sep="")

