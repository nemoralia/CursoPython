import random
options = ("piedra" , "papel" , "tijera")

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("Computer_Wins" , computer_wins)
    print("User_Wins" , user_wins)


    user_option = input("Piedra, papel o tijera ==> ")
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
        print ("===Esta opción no es válida===")
        continue

    computer_option = random.choice(options)

    print ("User Option =>", user_option)
    print ("Computer Option =>," , computer_option)

    if user_option == computer_option:
        print ("empate!")

    elif user_option == "piedra":
        if computer_option == "tijera":
            print ("gana piedra sobre tijera")
            print ("user ganó")
            user_wins += 1
        else:
            print("papel gana a la piedra")
            print("computador ganó")
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "piedra":
            print ("papel gana a piedra")
            print ("user ganó")
            user_wins += 1
        else: 
            print("piedra gana sobre papel")
            print ("computer ganó")
            computer_wins += 1

    elif user_option == "tijera":
        if computer_option== "papel":
            print ("tijera gana a papel")
            print ("user ganó")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("computer ganó") 
            computer_wins += 1

    if computer_wins == 2:
        print("El ganador fue la computadora")
        break
    if user_wins == 2:
        print("El ganador fue el usuario")
        break
    
