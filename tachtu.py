# sentences = input()
# sentence2 = ""
# for letter in sentences:
#     if letter == " ":
#         print(sentence2)
#         sentence2 = ""
#         print("\n")
#     else:
#         sentence2+=letter
#
# print(sentence2)


#Solution2

sentences = input()
sentence2 = sentences.split(" ")
for letter in sentence2:
    print(letter)
