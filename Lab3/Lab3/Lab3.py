#zad 1
paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo >= 0:
    print("paliwo", paliwo)
    print("Czas", czas)
    czas += 1
    paliwo -= paliwo_zuzyte_na_s

print("Koniec lotu...\n")

#zad 2
a = 2
i = 0
liczby_pierwsze = []

#while i < 10:
while i < 10:
    lPierwsza = True
    b = 2
    while b * b <= a:
        if a % b == 0:
            lPierwsza = False
            break
        b += 1
    if lPierwsza:
        liczby_pierwsze.append(a)
        i += 1
    a += 1

print(liczby_pierwsze, "\n")

#zad 3
nazwy_ulic = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
for ulica in nazwy_ulic:
    for blok in range(1, 6):
        for lokal in range(1, 11):
            print(f"ul. {ulica} {blok} {lokal}")

#zad 4
x = int(input("\nPodaj liczbę gości: "))
n = int(input("Podaj liczbę dań: "))

rachunek = 0
i = 0

while i < n:
    cena = float(input("Podaj cenę: "))
    rachunek += cena
    i += 1

print(f"Rachunek do zapłacenia na każdego gościa to: {rachunek/x}\n")

#zad 5
i = 0
while i < 4:
    for y in range(80, 0, -4):
        print(y)
        i += 1

#zad 6
a = int(input("\nPodaj liczbę: "))

while True:
    if a < 0:
        break
    else:
        a = int(input("Podaj liczbę: "))

#zad 7
#a)
n = int(input("Podaj liczbę studentów: "))
i = 0
srednia = 0

while i < n:
    p = int(input("Podaj liczbę punktów: "))
    srednia += p
    if p < 0 or p > 100:
        break
    else:
        i += 1

print(srednia/i)

# b)
while True:
    p = int(input("\nPodaj liczbę punktów: "))
    srednia += p
    if p < 0 or p > 100:
        break

print(srednia/i)

# zad 8
tekst = "Python jest super"
print(tekst[0])
print(tekst[-1])
print(tekst[:2])
print(tekst[1:2])
print(tekst[10:])
print(tekst[-1:])

#zad 9
imie = str(input("\nWitaj "))
print(imie)

wiek = int(input("\nTwój wiek to: "))
print(wiek)

imie = str(input("\nImie: "))
nazwisko = str(input("Nazwisko: "))
inicjaly = imie[0].upper() + ". " + nazwisko[0].upper() + "."
print(inicjaly)

a = str(input("\nWprowadź łańcuch: "))
i = 0

while i < 5:
    print(a)
    i += 1

b = str(input("\nŁańcych 1: "))
c = str(input("Lańcuch 2: "))
d = b+c

print(d)

la1 = str(input("\nŁańcych 1: "))
la2 = str(input("Lańcuch 2: "))

la3 = la1+la2
laLen = len(la3)/2
print(la3[0:round(laLen)])