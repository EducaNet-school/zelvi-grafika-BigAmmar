x = int(input('zadejte liche cislo:'))

liche_cisla=[]
liche_cislo = 1

for i in range(7):
    liche_cislo = liche_cislo +2
    liche_cisla.append(liche_cislo)

scitani = sum(liche_cisla)+x
print(sum(liche_cisla),'+',x,'=',scitani)
