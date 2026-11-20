#zad 1
from email.policy import default
from itertools import count
from math import sumprod
from multiprocessing import Value
import string
from tracemalloc import stop


Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
lista1 = [1, 14, 3, 5, 36, 4, 86, 90, 2, 21]
lista2 = [1, 17, 3, 53, 3, 46, 86, 90, 2, 221]

print(Moja_lista)
print(Moja_lista[0])
print(Moja_lista[-1])
print(len(Moja_lista))
print(max(Moja_lista))
print(min(Moja_lista))
print(sum(Moja_lista))
print(sorted(Moja_lista))
Moja_lista.append(6)
print(Moja_lista)
Moja_lista.insert(4, 5)
print(Moja_lista)
Moja_lista.pop()
print(Moja_lista)
Moja_lista.reverse()
print(Moja_lista)
listaL = lista1 + lista2
print(listaL)
listaM = lista1*5
print(listaM)
print(Moja_lista[:5])
print(Moja_lista[5:])
print(Moja_lista[2:5:1])
print(Moja_lista[::-1], "\n")

#zad 2
imiona = ["Izydor", "Mateusz", "Krystian", "Hans"]

#a
print(sorted(imiona))

#b
imiona.append("Zenon")
imiona.append("Gustaw")

print(imiona.pop())

#c
imiona.insert(3, "Teodor")

#d
#print(imiona.reverse() + imiona)

#zad 3
imie = str(input("Podaj imię: "))
nazwisko = str(input("Podaj nazwisko: "))
wiek = int(input("Podaj wiek: "))

print(f"Witaj {imie}\n")
print(f"Twój wiek to: {wiek}\n")
print(f"{imie[0]}.{nazwisko[0]}.\n")

lanc1 = str(input("Wczytaj 1 łańcuch: "))
lanc2 = str(input("Wczytaj 2 łańcuch: "))
lanc3 = lanc1 + lanc2

print(lanc3)

lanc4 = str(input("Wczytaj 4 łańcuch: "))
lanc5 = str(input("Wczytaj 5 łańcuch: "))
lanc6 = lanc4[:round(len(lanc4)/2)] + lanc5[:-round(len(lanc5)/2)]

print(lanc6, "\n")

#zad 4 - dodatkowe
zdanie = tuple(input("Podaj zdanie: "))
alfabet = tuple(string.ascii_letters)

print(sorted(zdanie), "\n")

not_in_zdanie = tuple(litera for litera in alfabet if litera not in zdanie)

print(sorted(not_in_zdanie), "\n")

#zad 5
tydzien = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
print(tydzien, "\n")

#zad 6
owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')

print(f"Liczba bananów wynosi: {owoce.count('banan')}")

#zad 7
moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)
print(sorted(moja_krotka), "\n")

#zad 8
stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

ilosc_stopni = len(stopnie)

Major_index = stopnie.index("Major")

if "Pułkownik" in stopnie:
    Pulkownik_wystepowanie = stopnie.index("Pułkownik")

print(f"{ilosc_stopni}\n{Major_index}\n{Pulkownik_wystepowanie}\n")

#zad 9
lista = {"Jabłko" : 5, "Gruszka" : 4}

wydatki = sum(lista.values())

print(lista, "\nWydatki:", wydatki, "zł")