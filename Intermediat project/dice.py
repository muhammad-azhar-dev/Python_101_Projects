import random

def roll_dice():
    return random.randint(1,6)

def main():
    print("Dice roller simulator")
    while True:
        print(f"You rolled: {roll_dice()}")
        cont = input("roll again ? (yes/no)").lower()
        if cont != "yes":
            print("Goodbye!")
            break
if __name__=="__main__":
    main()