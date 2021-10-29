forrásfájl = open('valaszok.txt')
lista = forrásfájl.readlines()
lista_végek_nélkül = []
for elem in lista:
    lista_végek_nélkül.append(elem.strip())
forrásfájl.close()
print(lista_végek_nélkül)