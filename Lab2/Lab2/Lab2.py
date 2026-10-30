#zad1
x = int(input("Podaj liczbę punktów: "))

if x > 80:
    print("Zaliczasz w I terminie.\n")
elif x >= 50 & x <= 80:
    print("Możesz poprawić swój wynik.\n")
else:
    print("Musisz poprawić swój wynik.\n")

#zad2
x = int(input("podaj x: "))
y = int(input("podaj y: "))
z = int(input("podaj z: "))

if x > y & x >z:
    print(x)
    if y > x & y > z:
        print(y)
        print(z)
    elif z > x & z > y:
        print(z)
        print(y)
elif y > x & y > z:
    print(y)
    if x > y & x > z:
        print(x)
        print(z)
    elif z > x & z > y:
        print(z)
        print(x)
elif z > x & z > y:
    print(z)
    if x > y & x > z:
        print(x)
        print(y)
    elif y > x & y > z:
        print(y)
        print(x)

#zad3
Nazwa_pliku = str(input("Podaj nazwę: "))

if ".xlsx" in Nazwa_pliku:
    print("Tak\n")
else:
    print("Nie\n")

#zad4
gol = int(input("Podaj liczbę goli: "))
bonus = gol * 10

#a)
if gol > 5 & gol < 10:
    bonus += 5
elif gol > 10:
    bonus += 10

print(f"Liczba zdobytych punktów: {bonus}\n")

#b)
if gol > 5 & gol < 10:
    bonus += 5
elif gol > 10:
    bonus += 15

print(f"Liczba zdobytych punktów: {bonus}\n")

#zad5
#a)
fp = open("notowania_gieldowe.txt", "r")
print(fp.read())
fp.close()
#b)
fp = open("notowania_gieldowe.txt", "a+")
fp.write("\nALR, 113")
fp.close()
fp = open("notowania_gieldowe.txt", "r")
print(fp.read())
fp.close()

#zad6
litera = str(input("\nPodaj literę: "))
if litera == litera.upper():
    print("Duża litera\n")
else:
    print("Mała litera\n")

#zad7
haslo = "pk47!jy0893"
hasloL = len(haslo)

if hasloL >= 11 and "!" in haslo:
    print("Hasło jest poprawne.\n")
else:
    print("Hasło nie poprawne.\n")

#zad8
text = 'Studiuje-Informatykę'
textList = list(text)
text3 = textList[:3]
text2 = textList[-3:]
print(f"{text3}\n{text2}")

#zad9
text = str(input("\nPodaj text: "))

text2 = text.swapcase()
    
print(f"\n{text2}")