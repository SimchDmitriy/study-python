word = str(input())
kol_simvolov = len(word)
id = int(kol_simvolov/2)
if kol_simvolov % 2 == 0:
    print(word[id-1] + word[id])
else:
    print(word[id])
