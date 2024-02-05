import random

guessNumber = random(1, 101)


while True:
    guess = int(input("Elija un numero del 1 al 100"))
    
    if guess < guessNumber:
        print(f"El numero es mayor a {guess}")
    elif guess > guessNumber:
        print(f"El numero es menor a {guess}")
    if guess == guessNumber:
        print("Felicidades Ganaste")
        print("Fin del juego")
        break