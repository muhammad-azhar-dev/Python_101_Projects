from textblob import TextBlob

def check_words(word):
    correct_word = TextBlob(word).correct()
    if word == correct_word:
        print(f"'{word}' is correct!")
    else:
        print(f"'{word}' is wrong!\nCorrect word is '{correct_word}'")


if __name__ == "__main__":
    word = input("Please write a word: ")
    check_words(word)