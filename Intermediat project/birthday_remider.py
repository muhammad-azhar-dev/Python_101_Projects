from datetime import datetime

def store_birthdays():
    birthdays = {}
    while True:
        name = input("Enter name (or 'quit' to stop): ")
        if name.lower() == 'quit':
            break
        birthday = input(f"Enter {name}'s birthday (YYYY-MM-DD): ")
        birthdays[name] = birthday
    return birthdays

def check_birthdays(birthdays):
    today = datetime.today().strftime('%Y-%m-%d')
    for name, birthday in birthdays.items():
        if birthday == today:
            print(f"Today is {name}'s birthday!'")

def main():
    print("Birthday Reminder")
    birthdays = store_birthdays()
    check_birthdays(birthdays)

if __name__=="__main__":
    main()