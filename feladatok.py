import random
import math
"""Kérj be A betűvel kezdődő nevet  a felhasználótól. 
Amennyiben nem A betűs nevet ad meg a felhasználó, akkor kérd be újra addig, amíg A betűs nevet nem ad meg!  
"""
def elsofeladat():
    nev = str(input("Adj meg egy nevet:"))
    
    while nev !="A":
        nev = str(input("Adj meg egy nevet:"))      


"""Írass ki a konzolra 5 db  [30, 50] zárt intervallumba eső véletlen számot. Hány 5-tel osztható van közöttük? A kiírás formátuma:
„A számok között X db 5-tel osztható van!”"""
def masodikfeladat():
    i = 0
    szamlalo = 0

    while i <= 5:
        szam = math.floor(random.random() * 49 + 30)
        print(f"számok:{szam}")
        if szam % 5 == 0:
            szamlalo += 1
    
        i += 1
    print(f"A számok között {szamlalo} db 5-el osztható szám van!")    
    return szamlalo

"""Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Írjuk ki a szöveg 2. karaktert N-szer a képernyőre!
"""
def harmadikfeladat(szoveg:str,szam:int):
    hossz=len(szoveg)
    if hossz < szam:
        print("Nincs  karakter!")
    
    else:
        print(szoveg.upper()[szam-1]*2) 

"""Írj metódust, mely számokat kér a felhasználótól, amíg a 0 nem ír.
Hány számot adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 számot adott meg.”
"""
def negyedikfeladat():
    szamlalo = 0
    szam = int(input("Adj meg egy számot:"))
    
    while szam !="0":
        szam = str(input("Adj meg egy számot:"))
        szamlalo += 1
    
    print(f"A felhasználó {szamlalo} számot adott meg.")
    return szamlalo

"""Szimuláljuk a számkitaláló játékot. 
Írj eljárást, amiben: 
A felhasználótól bekérjük a tippjét, ami 10 és 100 közötti egész szám lehet. Tárold el egy f_tipp váltopzóban.
Ezután a gép generál egy egész számot [10,100] között.  Tárold el a gep_tipp változóban
Ezután írd ki, hogy a felhasznáéló tippje kisebb, vagy nagyobb, mint a gép tippje, 
majd kérd be újra a felahsználó tippjét, amíg el nem találja a gép által gondolt számot!!
"""
def otodikfeladat():
    i = 0
    gep_tippje = math.floor(random.random()* 99 + 10)
    print([gep_tippje])
    felhasznalo_tippje = int(input("Kérlek válassz egy egész számot [10-100] között!"))
    while gep_tippje != felhasznalo_tippje:
        if gep_tippje > felhasznalo_tippje:
            print("A megadott szám kisebb mint a gép által megadott szám")
        if gep_tippje < felhasznalo_tippje:
            print("A megadott szám nagyobb mint a gép által megadott szám")
        felhasznalo_tippje = int(input("Kérlek válassz újra!"))

    print(f"Gratulálok, kitaláltad a számot![{gep_tippje}]")

            




"""    if gep_tippje > felhasznalo_tippje:
        felhasznalo_tippje = int(input("A szám kisebb mint a gép által megadott szám, kérlek válassz újra!"))
    if gep_tippje < felhasznalo_tippje:"""
