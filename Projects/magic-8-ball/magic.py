# Magic 8-Ball
# Python 3.5.1
# Written by alfredmuffin

from time import sleep
from random import randint

# list of responses
responses = ["Yes", "No", "Probably", "Maybe", "I don't think so", "Perhaps",
             "It's possible", "Yes, I think so", "That seems likely", "Sure",
             "That's not possible", "I would hope so", "Sounds like it could be true", 
             "You shoudn't do that", "But why?", "Dreadfully tinny word, that is", 
             "The cake is a lie!", "A man chooses. A slave obeys.", "Did you set it to Wumbo?", "42"]

def magic():
    question = input("Ask me a question: ")
    print("\nThinking ...")
    sleep(1)

    print(responses[randint(0, 20)], "\n")
    loop()

def loop():
    play = input("Would you like to play again? (Y/N) ").lower()

    if play == "y":
        Magic()

    elif play == "n":
        print("Goodbye!")

    else:
        print("I didn't quite catch that.")
        loop()

# welcome message
print("\nWelcome to the Magic 8 ball!")
magic()
