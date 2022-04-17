P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    k_board = input()
    distance = k_board.split(" ")
    if distance[0] == "0":
        break
    sentences = ""
    for i in range(0, len(distance[1])):
        for j in range(0, len(P)):
            if distance[1][i] == P[j]:
                sentences += P[(j + int(distance[0])) % 28]
    new_list = list(sentences)
    new_list.reverse()
    r_sentence = ""
    for i in range(0,len(new_list)):
        r_sentence += str(new_list[i])
    print(r_sentence)