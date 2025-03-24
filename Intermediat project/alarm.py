import time 
from datetime import datetime
current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)

def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Time to wake up!")
            break
        time.sleep(1)
def main():
    print("Set Your alarm clock")
    set_alarm()


if __name__ == "__main__":
    main()