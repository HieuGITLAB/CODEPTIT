sentence = input()
count = 0
for i in range(0, len(sentence)):
    if sentence[i] >= "a" and sentence[i] <= "z":
        count += 1

if count < len(sentence) - count:
    print(sentence.upper())
else:
    print(sentence.lower())
