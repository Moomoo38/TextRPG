import random

# when importing, its better to do it like below
# from the filename, import the specific class
from player import Player
from armor_item import ArmorItem
from enemy import Enemy

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


    # an example of creating a list
    enemies = []                        # initialize an empty list
    num_enemies = random.randint(2, 5)  # generate a random number from 1 to 5

    # for loop to create num_enemies amount of Enemy objects
    for i in range(num_enemies):        # this is equivalent to java's for (int i = 0; i < num_enemies; i++) { ... } 
        enemy = Enemy(str(i + 1), 5)    # ill just set the enemy object's name to its number
        enemies.append(enemy)           # add that enemy instance to the list

    # now we have a list of enemies we can do stuff to!
    def print_enemies():
        """
        take out enemies list and print out its info
        """
        for i in range(len(enemies)):   # iterate through the list of enemies
            enemy = enemies[i]          # single out the enemy at list index i
            print(f"enemy name: {enemy.name}, with health {enemy.health}")  # print out its information

    print_enemies()
    print("---- Applying some changes to the enemy list ----")
    enemies[0].name = "goblin"
    enemies[1].health -= 2
    print_enemies()

    # be careful, if you index something like enemies[7], you will get an index out of range error!

if __name__ == "__main__":
    main()