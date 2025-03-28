import random
import time
c_choice = random.randint(1, 100)
chances = 3

while chances > 0:
    u_choice = int(input("\nCHOOSE ANY NUMBER FROM 1 TO 100: "))
    print("---------------RESULT-------------")
    time.sleep(1)
    
    if u_choice == c_choice:
        print("CONGOO.... YOU GUESSED THE NUMBER RIGHT!!")
        break
    else:
        chances -= 1
        if u_choice > c_choice:
            time.sleep(1)
            print("\nOOPS!")
            time.sleep(0.5)
            print("\nHINT: Too high... Try again.")
            
        else:
            time.sleep(1)
            print("\nOOPS! ")
            time.sleep(0.5)
            print("\nHINT: Too low... Try again.")
            
        
        if chances > 0:
            time.sleep(0.5)
            print(f"You have {chances} chances left.")
        else:
            time.sleep(0.5)
            print(f"Sorry, you're out of chances! The correct number was {c_choice}.")
