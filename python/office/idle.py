
# Your code here
from random import choice

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = choice(coworkers)
    print("Chatting with " + chatee + "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    randChoice = choice(socialMedia)
    print("Using " + randChoice + "...")
    print("Done")
