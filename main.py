import random
a = "David"
b = "Žáček"
print(a +" "+ b)

c = int(input("Napište věk: "))
print(c)

d = len(a+b)
print(d)

e = 6


f = 0
for i in range(5):
    f += 3  
print(f)

vek = input("Zadejte svůj věk: ")

if vek.isdigit():
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")

nahodna_hodnota = random.randint(1, 10)
print(nahodna_hodnota)