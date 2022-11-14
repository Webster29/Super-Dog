print("Hello! Welcome to the story of our Super Dog! We have quite the adventure to tell you about today!")
print("First, I have to ask you a few questions.  Be sure to answer each one and press enter after!")
input("\nPress the enter key to continue...")

dog =input("\nWhat is our Super Dog's name?  ")
owner =input("\nWhat famous Hero adopted our Super Dog?  ")
city =input("\nWhat city does our Super Dog Protect?  ")
villain =input("\nWho is your favorite Super Villain?  ")
hero =input("\nWho is your favorite Super Hero? (Cannot be the same as Super Dog's owner.)  ")

print("\nOnward to our adventure!")
print("\nToday we visit our lovely city of " + city + ".")
print("Our famous Super Dog, " + dog + " has noticed his owner missing.")
print("Looks like " + owner + " has been captured by the Band of Villains!")
print("Our powerful friend, " + dog + ", must set out to find " + owner + " before it's too late!")

print("\nSuper Dog, " + dog + ", sets out to find " + owner + ".")
print("\nAlong the way, " + dog + " comes across a lone villain.")
print ("This villain is learned to be the devious " + villain + "!")

fightVillain = input("\nShould " + str(dog) + " fight the lone villain?  Type yes or no:  ")

if fightVillain == "yes":
    print(villain + " is trying to rob a bank for the precious diamonds!")
    print("If " + dog + " can stop " + villain + ", we can find the secret hideout for the Band of Villains!")
    print(dog + " uses his freeze breath to trap " + villain + "!")
    print("After a few minutes of questioning, " + dog + " gets a solid clue to finding the hideout!")
    print("\nNo time to lose!!!")
else:
    print("\n" + dog + " determines they do not have time to fight this time.")
    print(dog + " must find a way to save " + owner + ".")
    print(dog + " leaves " + villain + " to do is villainous duties at the bank.")
    print( villain + " robs the bank and gets away with precious diamonds!")

print("\nThe next step of our adventure brings us to a familiar face.")
print("We see " + hero + " squaring off with another group of villains.")

helpHero = input("\nShould " + str(dog) + " help " + hero + " fight this group of villains?  Type yes or no:  ")

if helpHero == "yes":
    print("\nIf we help " + hero + ", the League of Heroes may join our fight to rescue " + owner + "!")
    print(dog + " jumps into the fight and helps " + hero + " pummel his enemies!")
    print(hero + " agrees to call upon the League of Heroes to help save " + owner + ".")
    print("\nHang on " + owner + "! We will find you!")
else:
    print("\n" + dog + " does not want to waste time with this fight and chooses not to engage.")
    print(hero + " fends off the group of villains all alone!")
    print("Because " + dog + " left the fight, the League of Heroes have no idea that " + owner + " has been captured.")
    print("Looks like " + dog + " is on their own!")

if fightVillain == "yes" and helpHero == "yes":
    print("\nWith the League of Heroes with us and the clue from stopping " + villain + ",")
    print("we can set forth our efforts to find " + owner + ".")
    print("\nWithin the next hour, " + dog + " spots " + owner + " through a wall using his X-Ray Vision!")
    print(dog + ", along with " + hero + " and the League of Heroes, bust into the hideout of the Band of Villains.")
    print(dog + " uses their laser eyes and freeze breath!")
    print(dog + " is able to rescue " + owner + " without them getting hurt! ")
    print("The League of Heroes captured the Band of Villains and took them all to jail!")
    print("\n" + dog + " and " + owner + " set off for home for much deserved rest!")
    print("\n" + city + " can rest easy now knowing " + owner + " is safe and soon ready to fight crime again with " + dog + " at their side!")
elif fightVillain == "yes":
    print("\nAfter spending the day in " + city + ", " + owner + " was located at the Band of Villains' secret hideout!")
    print(dog + " fought alone and bravely and ultimately saved " + owner + "!")
    print("Because " + dog + " did not help " + hero + ", the League of Heroes did not come to the fight.")
    print("Both "+ dog + " and " + owner + " rushed to seek medical attention.")
    print(dog + " and " + owner + " were back to protecting " + city + "after a few short weeks of recovery!")
else:
    print("\n" + dog + " did not get any intel from " + villain + " and no help from the League of Heroes.")
    print(dog + " could not locate " + owner + " despite his efforts to search high and low.")
    print("Will " + owner + " ever be seen again?")
    print("Who will protect " + city + " without " + owner + "?")
    print("(\n)")

    