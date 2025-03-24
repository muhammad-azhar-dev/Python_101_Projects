import random

# Load words from file
def load_words(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().splitlines()
            if not words:
                print("The word list is empty. Please add words to the file.")
            return words
    except FileNotFoundError:
        print("Word file not found! Please ensure the file exists.")
        return []

# Hangman game logic
def play_hangman(words):
    word = random.choice(words).lower()
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("\nWelcome to Hangman!")
    print("Guess the word by entering one letter at a time.")

    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print(f"Guesses left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}" if guessed_letters else "No guesses yet.")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            guessed_letters.add(guess)
        else:
            print("Incorrect.")
            attempts -= 1
            guessed_letters.add(guess)

    if "_" not in guessed_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word} 🎉")
    else:
        print(f"\n😞 Game over! The word was: {word} 😞")

# Main function
def main():
    print("Hangman Game")
    words = load_words("words.txt")  # Ensure 'words.txt' exists with words in it
    if not words:
        return

    while True:
        play_hangman(words)
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
