import random
import math

#zad1
#a)
print(1+2)              #dodawanie liczb całkowitych
print(1+4.5)            #dodawanie liczb zmiennoprzecinkowych
print(3/2)              #dzielenie przez liczbę nieparzystą
print(4/2)              #dzielenie przez liczbę parzystą
print(3//2)             #dzielenie całkowite przez liczbę nieparzystą
print(-3//2)            #dzielenie całkowite przez liczbę nieparzystą ujemną
print(11%2)             #modulo (reszta z dzielenia)
print(2**10)            #potęgowanie
print(8**(1/3), "\n")   #potęgowanie przez ułamek
#b)
print(int(3.0))         #zdefiniowanie wartości jako integer (liczba załkowita)
print(float(3))         #zdefiniowanie wartości jako float (liczba zmiennoprzecinkowa)
print(float("3"))       #zdefiniowanie wartości jako float (liczba zmiennoprzecinkowa)
print(str(12.4))        #zdefiniowanie wartości jako string (łańcuch znaków)
print(bool(0), "\n")    #zdefiniowanie wartości jako bool (wartość logiczną, true albo false)

#zad2
uczelnia = "Studjuję na WSIiZ"
print(uczelnia, "\n")

#zad3
imię = 'Jan'
wiek = 20
wzrost = 178

print("Nazywam się", imię, "i mam", wiek, "lat.\nMój wzrost to", wzrost, "cm.\n")

#zad4
Cena = 39.99
Rabat = 0.2
zRabatem = Cena - Cena * Rabat

print(round(zRabatem, 2), "zł\n")

#zad5
a = int(input("Podaj długość a: "))
b = int(input("Podaj długość b: "))
pole = a*b
obw = 2*a + 2*b

print("Pole prostokąta to: ", pole, "\nObwód prostokąta to: ", obw, "\n")

#zad6
droga = float(input("Podaj pokonaną drogę: "))
spalanie = float(input("Podaj średnie spalanie: ")) #na 100km
cena = 6.5 #zł/l

koszt = (droga * (spalanie / 100)) * cena

print("Koszt podróży to: ", round(koszt, 2), "zł\n")

#A)
drogaA = random.randint(1, 1000)
cenaA = float(input("Podaj cenę paliwa: "))

print("Koszt podróży to: ", round(koszt, 2), "zł\n")

#B)
print(f"Koszt podróży to: {round(koszt, 2)}zł\n")

#zad7
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

print(f"{a}x+{b}=0")
bb = b*(-1)
print(f"{a}x={bb}")
x = bb/a
print(f"x={x}\n")

#zad8
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("Nie ma rozwiązania równania.\n")
elif delta == 0:
    x = -b/(2*a)
    print("x=", x, "\n")
else:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("x1=", round(x1, 1), "\nx2=", round(x2, 1), "\n")

#zad9
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
mnozenie = liczba1 * liczba2
dzielenie = liczba1 / liczba2
potega = liczba1 ** liczba2

print(f"Wynik dodawania: {dodawanie}\nWynika odejmowania: {odejmowanie}\nWynik mnożenia: {mnozenie}\nWynik dzielenia: {dzielenie}\nWynik potęgowania: {potega}\n")