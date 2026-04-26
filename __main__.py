import Player

#IDEAS:
#Using here to take notes of possible general ideas, probably should put this somewhere else but y'know I can do what I want
#Considering adding "scrying" as a random one time spell the player can get as a rare reward, which would let them view possible outcomes of each choice in the current event

def main():
    player = Player.Player()
    player.create_character()
    print(player)

if __name__ == "__main__":
    main()