age = input("Quel est votre âge ?: ")
result1 = 7
result2 = 12
if age < str(18):
    result = result1
else:
    result = result2
print("Votre place est de " + str(result) + "euros")

pop_corn = input("Voulez-vous des popcorns: ")
Yes = str(1)
No = str(0)
if pop_corn == Yes:
    result_pop_corn = result + 5
else:
    result_pop_corn = result

print("Votre total à payer est de " + str(result_pop_corn) + " euros")
