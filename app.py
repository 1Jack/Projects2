# rewritten by W.Anderson 14/12/2020
# freeCodeCamp.org https://www.youtube.com/watch?v=8ext9G7xspg
# string concatenation (aka how to put strings together)
# supoose we want to create a string tha says "subscribe to ________"
youtuber = " Winstone " # some string variable

 # different ways of doing this
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Who are you?: ")
verb1 = input("what do you like to do?: ")
verb2 = input("What is your fav colour?: ")
famous_person = input("Who are you?: ")


app = f"I am the best person the ever lived {adj} Wish I could {verb1} all day and \
     I just love to look at this colour all day  {verb2} all day and night. you a {famous_person}" 
print(app)