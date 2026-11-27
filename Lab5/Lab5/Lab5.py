#zad 1
import math

a = int(input("Podaj liczbę: "))

def kwadrat(a):
    return a ** 2

print(f"Kwadrat liczby wynosi: {kwadrat(a)}\n")

#zad 2
tekst = str(input("Podaj tekst do odwrócenia: "))

def odw_str(tekst):
    return tekst[::-1]

print(f"Odwrócony tekst: {odw_str(tekst)}\n")

#zad 3
def powitanie(imie = "Użytkowniku", jezyk = "polski"):
    if jezyk == "polski":   print(f"Cześć, {imie}\n")
    elif jezyk == "angielski":  print(f"Hello, {imie}\n")
    elif jezyk == "niemiecki":  print(f"Guten Morgen, {imie}\n")
    else:   print(f"Witaj, {imie}\n")

powitanie("Adam", "angielski")

#zad 4
liczby = [1,2,3,4]

def srednia(liczby):
    wynik = 0
    i = 0
    while i < len(liczby):
        wynik += liczby[i]
        i += 1

    return wynik / len(liczby)

print(f"Srednia liczb z listy wynsi: {srednia(liczby)}\n")

#zad 5
waga = float(input("Podaj wagę: "))
wzrost = float(input("Podaj wzrost: "))

def BMI(waga, wzrost):
    return waga / (wzrost ** 2)
    
bmi = round(BMI(waga, wzrost), 2)

if bmi < 18.5:  print(f"Niedowaga\n")
elif bmi >= 18.5 and bmi <= 24.9:  print(f"Prawidłowa masa ciała\n")
elif bmi >= 25 and bmi <= 29.9:  print(f"Pożądana masa ciała\n")
elif bmi >= 30 and bmi <= 34.9:  print(f"Otyłość I stopnia\n")
elif bmi >= 35 and bmi <= 39.9:  print(f"Otyłość II stopnia\n")
elif bmi >= 40:  print(f"Otyłość III stopnia\n")

#zad 6
def pole(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))

    wynik = pole(a, b , c)

    print(f"Pole wynosi: {wynik}\n")
except ValueError:
    print(f"Błędne dane!\n")

#zad 7
n = int(input("Podaj stopień potęgi: "))
a = int(input("Podaj liczbę: "))

def potegowanie(n, a):
    if n == 0:
        return 1
    else:
        return a * potegowanie(n - 1, a)

print(f"Wynik potęgowania to: {potegowanie(n, a)}\n")

#zad 8
#a)
def zmienne1(*args):
    print(args, "\n")

zmienne1(2, 5, 6, 4, 7)

#b)
def zmienne2(*args):
    return max(args)

print(zmienne2(10, 5, 1, 4, 7), "\n")

#zad 9
n = int(input("Który element ciągu wskazać: "))

def ciag(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciag(n - 1) + ciag(n - 2)

print(f"Element {n} to: {ciag(n)}\n")

#zad 10
def funSekw(sekw1, sekw2):
    return list(set(sekw1) & set(sekw2))

wart1 = (1, 2, 4, 6, 8, 10)
wart2 = (1, 2, 4, 8, 16, 32)

print(funSekw(wart1, wart2), "\n")