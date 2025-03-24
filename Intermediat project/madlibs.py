def mad_libs():
    print("Welcome to the Mad Libs Game!")

    adj1 = input("Enter an Adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")

    story = f"Today I went to the {adj1} {noun1} and saw a {adj2} {noun2}. I decided to {verb1} it!"

    print("\nHere is your story: \n")
    print(story)

def main():
    mad_libs()
if __name__ == "__main__":
    main()