a = "Hello world"

b = 20

c = 20.1

d = False

print(a)

name = input("What is your name? ")
print("my name is " + name)


def PrintFunction():
    print(a)
    print(b)
    print(c)
    print(d)
PrintFunction()

def ifStatementExample():
    if(d == True):
        print("because d is set to true on line 4, this option prints")
    else:
            print("if d was not true, this statement will print. ")

ifStatementExample()

feeling = input("How are you today? ")
if "good" in feeling:
    print("im feeling pretty good too!")
elif "amazing" in feeling:
    print("thats fantastic!")
else:
    print("sorry to hear that")

BestMovie = "Spongebob"

MovieChoice = input ("What is your favourite movie? ")
if (MovieChoice ==  BestMovie):
    print ("Thats cool my favourite is spongebob too bro ")
else:
        print ("Oh !" + MovieChoice +" that movie is terrible my favourite is " + BestMovie +"!")


BestSong = "ditty"

SongChoice = input ("What is your favourite song? ")
if (SongChoice ==  BestSong):
    print ("Thats cool my favourite is ditty too bro ")
else:
        print ("oh cool" + SongChoice +" that song is terrible my favourite is " + BestSong +"!")

        
positive_feelings = ["happy", "joy", "gratitude",
                     "hope", "love", "awe", "love"]
print (positive_feelings[0])





