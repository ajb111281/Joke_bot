import random
import time
import sys

def type_out(text, delay=0.05):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

Affirmative = "YES"
Negative = "NO"

jokes = ["I told my doctor that I broke my arm in two places, he told me to stop going to those places.",
         "I broke a finger on my left hand, on the other hand I'm all right.",
         "My uncle has the heart of a lion, he also has a lifetime ban from the zoo.",
         "I used to play piano by ear, but now I use my hands.",
         "Parallel lines have so much in common, it's a shame they will never meet.",
         "I used to be addicted to soap, but I'm clean now.",
         "My boss told me to have a good day. So I went home.",
         "I once got into a fight with a broken elevator, I took it to another level",
         "I only know 25 letters of the alphabet, I don't know Y"
         ]

dismiss = ["Take this straw and got suck the fun out of somewhere else",
           "Your loss!",
           "That's okay, I didn't want to waste a joke on you anyways!",
           ]






type_out("Welcome to Joke-Bot")
type_out("\nWhat is your name?\n")

name = input().upper()

type_out(f"Nice to meet you, {name}!")
while True:
    type_out("\nDo you want to hear a joke? ")
    answer = input().upper()
    if answer in Affirmative:
         type_out(random.choice(jokes))
         break
    elif answer in Negative:
         type_out(random.choice(dismiss))
         time.sleep(10)
         sys.exit()
    else:
          type_out("Please answer YES or No.")

while True:
    type_out("\nDo you want to hear another joke? ")
    answer = input().upper()

    if answer in Affirmative:
         type_out(random.choice(jokes))
    elif answer in Negative:
         type_out(random.choice(dismiss))
         time.sleep(15)
         break
    
    else:
         type_out("Please answer Yes or No!")



         




