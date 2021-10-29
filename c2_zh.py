#1.feladat
valaszok = []
forrásfájl = open('valaszok.txt')
for sor in forrásfájl:
    valaszok.append(sor.strip())
forrásfájl.close()
print("1. feladat: Az adatok beolvasása.")

#2.feladat
versenyzok_szama = (len(valaszok)-1)
print("2. feladat: A versenyen",versenyzok_szama,"versenyző indult.")

#3.feladat
bekert_nev = input("3. feladat: Kérem adja meg a versenyző azonosítóját:")

for a in range(len(valaszok)):
    if bekert_nev in valaszok[a]:
        versenyzo_es_eredmeny = valaszok[a]
        eredmeny = versenyzo_es_eredmeny[6:20]
        print(eredmeny)
    if bekert_nev not in valaszok[a]:
        versenyzok_szama -= 1
if versenyzok_szama < 0:
    print("Ilyen kóddal nem indult versenyző.")

#4.feladat
helyes_megoldas = valaszok[0]
pontozas = []
print("4. feladat: A helyes megoldás:")
print(helyes_megoldas)

if versenyzok_szama < 0:
    eredmeny_seged = valaszok[1]
    eredmeny = eredmeny_seged[6:20]
for b in range(len(helyes_megoldas)):
    if helyes_megoldas[b] == eredmeny[b]:
        pontozas.append('+')
    if helyes_megoldas[b] != eredmeny[b]:
        pontozas.append(' ')
print(pontozas)

#5.feladat
feladat_sorszam = int(input("5. feladat: Kérem adja meg a feladat sorszámát:"))
eltalalt_feladatok_szama = 0
c = 1

for c in range(len(valaszok)):
    vizsgalt_versenyzo_eredmenye = valaszok[c]
    if vizsgalt_versenyzo_eredmenye[feladat_sorszam] == helyes_megoldas[feladat_sorszam]:
        eltalalt_feladatok_szama += 1

eltalalt_feladatok_szazalekban = (versenyzok_szama/100)*eltalalt_feladatok_szama

print("A feladatra",eltalalt_feladatok_szama,"fő, a versenyzők",eltalalt_feladatok_szazalekban,"%-a adott helyes választ.")

#6.feladat

versenyzok_es_pontszamuk = []

for d in range(len(valaszok[1:305])):
    pontszam = 0
    eredmeny_es_nev_seged = valaszok[d]
    nev = eredmeny_es_nev_seged[0:6]
    eredmeny = eredmeny_es_nev_seged[6:20]
    for e in range(len(eredmeny)):
        if e == 1 or 2 or 3 or 4 or 5:
            if eredmeny[e] == helyes_megoldas[e]:
                pontszam += 3
        if e == 6 or 7 or 8 or 9 or 10:
            if eredmeny[e] == helyes_megoldas[e]:
                pontszam += 4
        if e == 11 or 12 or 13:
            if eredmeny[e] == helyes_megoldas[e]:
                pontszam += 5
        if e == 14:
            if eredmeny[e] == helyes_megoldas[e]:
                pontszam += 6
    versenyzok_es_pontszamuk.append(nev)
    versenyzok_es_pontszamuk.append(pontszam)
print(versenyzok_es_pontszamuk)

#7.feladat
print("7. feladat: A verseny legjobbjai:")
print(len(versenyzok_es_pontszamuk))
print(len(valaszok))
legnagyobb_pontszam = 0
f = 1
while f <= len(versenyzok_es_pontszamuk):
    if versenyzok_es_pontszamuk[f] > legnagyobb_pontszam:
        legnagyobb_pontszam = versenyzok_es_pontszamuk[f]
    f += 2
print(legnagyobb_pontszam)









