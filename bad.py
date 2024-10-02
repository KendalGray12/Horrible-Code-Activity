import random

# Bad practice: Everything is crammed into one function
def fortune_teller():
    # Bad practice: Directly gathering input inside the main function instead of a separate input function.
    name = input("Enter your name: ")
    
    # Bad practice: Hardcoding specific name logic for "Kendal"
    if name == "Kendal":  
        print("Hey Kendal here is a fortune just for you")
        print("Today is the day!")
    # Bad practice: logic based on the length of the name which doesn't have a strong reasoning.
    elif len(name) > 5:
        print(f"{name}, your fortune is: Success is on the way.")
    else:
        # Bad practice: The list of fortunes is hardcoded inside the main function.
        fortunes = [
            "You will have a great day!",
            "Great success is in your future!",
            "Watch out for all signs!",
            "Good news is headed your way!"
        ]
        # Bad practice: Repetitive code. 
        print(f"{name}, your fortune is: {random.choice(fortunes)}")

# Bad practice: The entire logic is crammed into one large block of the code.
fortune_teller()
