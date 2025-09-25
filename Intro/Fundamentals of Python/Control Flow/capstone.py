import random

# Ask for user input
name = input("Enter your name: ").strip()
question = input("Ask a Yes or No question: ").strip()

# Initialize answer variable
answer = ""

# Generate random number between 1 and 9
random_number = random.randint(1, 9)

# Uncomment the line below for testing random number generation
# print("Random number:", random_number)

# Magic 8-Ball responses
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Handle empty question input
if question == "":
    print("You need to ask a question to receive a fortune!")
else:
    # Handle empty name input
    if name == "":
        print(f"Question: {question}")
    else:
        print(f"{name} asks: {question}")

    print(f"Magic 8-Ball's answer: {answer}")
