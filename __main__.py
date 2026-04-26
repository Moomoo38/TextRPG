# when importing, its better to do it like below
# from the filename, import the specific class
from player import Player
from armor_item import ArmorItem

#IDEAS:
#Using here to take notes of possible general ideas, probably should put this somewhere else but y'know I can do what I want
#Considering adding "scrying" as a random one time spell the player can get as a rare reward, which would let them view possible outcomes of each choice in the current event

def main():
    player = Player()
    player.create_character()
    print(player)

    # create an example ArmorItem
    helmet = ArmorItem("Iron Helmet", "helmet", 2, 0, 0, 0, 0) # the 2, 0, 0, 0, 0 is an example of magic numbers, its bad programming. look it up to see what that means. this is just a test so it doesnt matter
    print(helmet) # invokes the __str__() function in Item superclass! you can override this function by having a __str__ in the ArmorItem class

    # test out the take_damage method
    player.take_damage(2)
    player.take_damage(4)

if __name__ == "__main__":
    main()