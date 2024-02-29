

def find_number(bottom: int, top: int):
    guessed = False
    while not guessed:
        guess = (bottom + top)//2
        answer = input(f"Is the number {guess}? (yes/no)")
        if answer == "yes":
            print("I got it! Awesome! Thanks for playing!")
            guessed = True
        elif answer == "no":
            while True:
                high_low = input("Was that too high or too low (too high or too low): ")
                if high_low == "too high":
                    top = guess
                    break
                elif high_low == "too low":
                    bottom = guess
                    break
                else:
                    print("I don't understand that. Please try again.")
        else:
            print("I don't understand that. Please try again.")

def main():
    print("Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
    
    ready = input("Are you ready? (yes or no)")
    
    while True:
        if ready == "yes":
            print("What range should I guess in?") 
            bottom = int(input("Give me the lowest possible number: "))
            top = int(input("Give me the highest possible number: "))
            find_number(bottom, top)
            break
        elif ready == "no":
            ready = input("Ok, no problem! Let me know when you are! (yes)")
        else:
            print("I don't understand that. Please try again.")
            ready = input("Are you ready? (yes or no)")

if __name__ == "__main__":
    main()
