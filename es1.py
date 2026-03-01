# print ("Hallo World!")

# def mia_funzione(argomento1, argomento2):
#     print(f"Argomenti: {argomento1} e {argomento2}")

# print(mia_funzione)

# # Esercizio 1:

# def convert_to_hours(minutes):
#     hours = int(minutes / 60)
#     return hours

# def rest_minutes(minutes):
#     hours = int(minutes / 60)
#     rest = minutes - (hours * 60)
#     return rest

# print(convert_to_hours(538),rest_minutes(538), sep = "h:", end = "min\n")

# Esercizio 2:

# number = int(input("Inserire il numero: "))

# def quadrato(number):
#     quadrato = number * number
#     return quadrato

# quad1 = quadrato(number)

# def cubo(number):
#     cubo = number * number * number
#     return cubo

# cub1 = cubo(number)

# print(quad1, cub1, sep = ",")

# Esercizio 3:

# number = int(input("Inserire il numero: "))

# if number%2 == 0:
#     print("Il numero è pari")
# else:
#     print("Il numero è dispari")

# Eserzio 4:

# word = (input("Inserire una parola: "))
# letter = (input("Inserire una lettera: "))

# def parola(x, y):
#     sum = 0
#     for i in x:
#         if i == y:
#             sum = sum + 1
#     return sum

# somma = parola(word, letter)
# print(somma)

# Esercizio 5:

# number = int(input("Inserire il numero: "))

# def is_prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#         else:
#             return True
        
# if is_prime(number):
#     print(str(number), "è primo", sep = " ")
# else:
#     print(str(number), "non è primo", sep = " ")

# Esercizio 6:

# number = int(input("Inserire il numero: "))
# sum = 0

# while number != 0:
#     sum = sum + number
#     number = int(input("Inserire il numero: "))

# print("La somma è: ", sum)

# Esercizio 7:

# number = int(input("Inserire il numero: "))

# def fattoriale (x):
#     prod = 1
#     for i in range(1,(x+1)):
#         prod = prod * i
#     return prod

# prodotto = fattoriale(number)
# print (prodotto)

# Esercizio 8:

# number1 = int(input("Inserire il 1 numero: "))
# number2 = int(input("Inserire il 2 numero: "))
# number3 = int(input("Inserire il 3 numero: "))

# def tipo_triangolo(x,y,z):
#     if (x<=0 or y<=0 or z<=0):
#         return False
#     elif (x+y <= z or x+z <= y or y+z <= x):
#         return ("Il triangolo non esiste")
#     elif (x == y == z):
#         return ("Il triangolo è equilatero")
#     elif (x == y or x == z or y == z):
#         return ("Il triangolo è isoscele")
#     elif (x != y != z):
#         return ("Il triangolo è scaleno")

# triangolo = tipo_triangolo(number1, number2, number3)
# print(triangolo)

# Esercizio 9:

stringa = str(input("Inserire una stringa: "))

def nr_vocali(frase):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    conta = 0
    for k in frase:
        if (a == k or e == k or i == k or o == k or u == k):
            conta = conta + 1
    return conta
        
vocali = nr_vocali(stringa)
print(vocali)