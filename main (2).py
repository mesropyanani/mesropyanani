import time

# function to take input from user
def get_input():
    while True:
        user_input = input("Enter time in seconds: ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

# function to start countdown
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")

# get time input from user
time_input = get_input()

# start countdown
countdown(time_input)