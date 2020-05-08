
from random import shuffle

word_to_show = input("Entrez autant de mots à retenir que vous voulez séparé par (-)").split("-")

print(word_to_show)

shuffle(word_to_show)

print(word_to_show)

if len(word_to_show) < 10:
    print(word_to_show[0:2])

else:
    print(word_to_show[-3], word_to_show[-2], word_to_show[-1])
