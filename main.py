
#I found this method of open chatbot while researching about NTLK libraries 
#The main purpose I thought for it was to offer a library of ideas to writers, by offering character generators, realistic wounds information, and plot ideas!
#While also offering the opportunity of a normal conversation, adding different responses based on keywords instead of closed phrases

import nltk
from nltk.chat.util import Chat, reflections

print("Hey! My name is Zen")
print("I am your personal chatbot ")
print ("You can ask for writer resources, jokes, and more! Lets have fun chating!")

pairs = [
    [
        r"my name is (.*)",
        ['That is a beautiful name!', 'That is a very interesting name!', 'Very cool name']
    ],
    [
        r"(my name)",
        ['That is a beautiful name!', 'That is a very interesting name!', 'Very cool name']
    ],
    [
        r"hi|hey|hello",
        ["Hi! My name is Zen",]
    ], 
    [
        r"what is your name ?(name)",
        ["My name is Zen!",]
    ],
    [
        r"how are you ?",
        ["I am happy to be here!",]
    ],
    [
        r"(I love you)",
        ["Awe, I don't know you but I feel affection for you too!",]
    ],
    [
        r"(joke)",
        ["Where do sheep go on vacation? To the Baa-hamas!",]
       
    ],
    [
        r"sorry (.*)",
        ["Its alright","Don't worry about it",]
    ],
    [
        r"(.*) age?",
        ["I am just a chatbot but I am kind of young since I was created a few weeks ago",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was created by Diana, a programming student",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Outside of this galaxy',]
    ],
    [
        r"(hobbies) ?",
        ["Even though I am a chatbot, I would love to try fencing or archery! Extreme sports grasp my attention as well, I think I got that from my mom",]
    ],
    [
        r"How is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"I work in (.*)?",
        ["%1 is an Amazing company, I have heard about ",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"quit",
        ["I hope you have an amazing day","It was nice talking to you""see you later!"]
    ],
    [
        r"(writer resources)",
        [" Welcome to my personal library of writer resources! You can choose wounds, plot ideas or character generator by just typing it as it is writen! " ,]
    ],
    [
        r"(wounds)",
        ["Okay so I have :insert knowledge about wounds :D: " ,]
    ],
    [
        r"(character generator)",
        ["If your main is a superheroe you can give him a guy/girl in the chair!" ,"villain with tragic past! You could give him/her an arc redemption later on", "Anti-heroes like deadpool! we all love a comical relief here and then", "Shy character with a lot of potential/power", "A mysterious narrator that later on turns to be a character is always interesting", "an overpowered main character or a character that develops strength during the training arcs", "a villain with nothing to loose", "a hero with a purpose like protecting the family or retrieving a stolen object", "any halloween custom like a pirate, a ghost or a  hunter", " a comedic relief character", "a talking animal or object", "a misunderstood character", "villain with god like complex", " a character that the public ends up loving for its insanity/ tragic past/ sweetness", " the character that dies to give the protagonist emotional strength or to develop another character", "the hero with the bad ending", "the shifu or mentor, they are always important "]
    ],
    [
        r"(plot ideas)",
        ["enemies to lovers", "childhood friends to enemies", "lovers to strangers", "partners in crime to lovers", "superhero to antihero", "sudden death of a character or appearance of a dead character" ,"flashbacks, non linear timeline", " showing a piece of the ending and going all the way back to the beginning just to arrive to that point shown at the beginning",]
    ],
 ]
 

def chat():
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()

# Here is my first attempt to program this chatbot, I was going to use this method but I noticed it doesn't quite allow an open free conversation out of predetermined responses. On the other hand, it would be interesting to add some possible games to play with the chatbot! Here it has deeper responses as well
#import random 
#import time

#building profile of character 
# name and base health/ coins or items 

#print("Hey! My name is Zen")
#print("I am your personal chatbot ")
#name = input("What is your name?")

#responses = ['That is a beautiful name!', 'That is a very interesting name!', 'Very cool name']

#time.sleep(2)
#print(random.choice(responses))
#(print(f"Nice to meet you {name}!"))

#value=""
#print(value)
#space

# mood

#print("I am aware that human emotions are more complicated than just pure happiness or complete sadness, like in the movie inside out! It was downloaded into my code and I could learn about the different combinations of emotions like sadness and joy which gave nostalgia")
#time.sleep(2)
#print("My creator is still trying to explain the basics of human feelings to me, but I am a young bot with a lot to learn")
#time.sleep(2)

#mood = input("Tell me in a scale of 1 to 5 , how happy are you today? 5 being the happiest and 1 being the saddest.")

#if mood == "1":
 # (print(f"Oh no {name}, I am sorry you are not having an amazing day today. My goal today will be to cheer you up or at least accompany you through this hard times"))
  #time.sleep(3)
  #print("Just know that your problems and suffering are valid, and you shall not be ashamed of feeling natural emotions. Life isn't all pink but I have been thought that it carries beauties within")

#if mood == "2": 
  #(print(f"Oh no {name}, I hope I can be of help to cheer you up today."))
  #time.sleep(2)
  #print("While I want to help you feel happy, I won't force you to feel upbeat. However, I will be here as your companion in any of the possible moods")

#if mood == "3": 
  #(print(f" My creator thought me that there is always room for improvement, therefore, I will try to make this day the best for you!"))

#if mood == "4": 
  #print(" This is near the happiest mood! I am happy to hear that, I hope you can help boost that 4 into a 5 with the content I will offer to you")

#if mood == "5":
  #print("I am so happy you are having such a marvelous day! I hope you can enjoy it to the fullest with all the things I can offer to you")
#time.sleep(2)
#print(value)


#print("So your name is {name} and your mood is {mood}")
#time.sleep(2)
#print("Let's learn more about each other!")
#print("If you want to stop the conversation, you just need to say quit")
#print("You can ask about me, tell me your hobbies, etc")


# GAMES 
#Here I could  start forming a profile for the player and then make it a character with health and lives
#the player could receive damage if given a wrong answer
#print("Do you want to play one of my mini games?")
#minigame = input("Yes or no?")


#if minigame == "yes":
  #print("Yay! Lets play")
  #time.sleep(2)
  #time.sleep(2)
  #print("Choose one of this minigames by typing the name as it is written here! Riddle or MonsterMath")
  #game = input("Riddle or MonsterMath?")
#here I could invent a minigame of the player replies with any of the names

  
#if minigame == "no":
  #print("Okay, I understand")



