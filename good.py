# By: Kendal Gray
# Date: 10/2/2024

import random

# Function to prompt for user's name with a different approach
def prompt_user_name():
    user_name = input("What's your name, dear user? ")
    return user_name.capitalize()

# Function to randomly select a fortune from the list
def pick_random_fortune():
    fortune_list = [
        "Today will bring a pleasant surprise!",
        "Challenges may arise, but you'll overcome them.",
        "An exciting opportunity is just around the corner.",
        "Prepare for a wonderful turn of events!"
    ]
    return random.choice(fortune_list)

# Function shhows different format
def show_fortune(name, fortune):
    print(f"Hello {name}, here’s your fortune: \"{fortune}\"")

def main():
    user_name = prompt_user_name()
    selected_fortune = pick_random_fortune()
    show_fortune(user_name, selected_fortune)

# Run the program
if __name__ == "__main__":
    main()
