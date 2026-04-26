class Player:
    def __init__(self):
        """
        note to michael: these strings denoted by triple quotes are called doc strings, used to document functions.
        you should make sure to write these for every function and explain the function, its arguments, etc.
        its an important skill to write good documentation for a codebase and is good etiquette for people reading your code. like me

        initialize an empty Player instance
        """
        self.name = ""
        self.health = 0
        self.defense = 0
        self.stats = {
            "constitution": 0,
            "resilience": 0,
            "strength": 0,
            "agility": 0
        }
    

    def create_character(self):
        """
        prompts the user to input player information
        """
        self.name = input("What is your name? ")
        print("\nYou may spend 5 points between your stats \n1. constitution (health)\n2. resilience (defense)\n3. strength (attack)\n4. agility (dodge)\n")
        points = 5

        while points > 0:
            self.level_up()
            points -= 1
    

    def level_up(self):
        """
        prompts the user to choose a stat to level up
        """
        try_again = True

        while try_again:
            try_again = False
            choice = input("What do you want to level up? ")
            match choice:
                case "1":
                    self.stats["constitution"] += 1
                case "2":
                    self.stats["resilience"] += 1
                case "3":
                    self.stats["strength"] += 1
                case "4":
                    self.stats["agility"] += 1
                case _:
                    print("Invalid selection, please input again")
                    try_again = True


    def take_damage(self, damage_taken):
        """
        method to handle damage dealt to the player

        Args:
            damage_taken (int): the amount of damage the player should take
        """
        # old code: bugs here that could happen, damage could heal the player if resilience is higher than damage.
        # also you didnt call the stat dict for resilience value, will cause null error
        # you call the min function here, so if player health is greater than 0 after applying damage,
        # the min function will set player health to 0 anyways, killing the player instantly!
        # remember: min(a, b) takes the lowest number between a and b, in this case it will always pick 0
        # you can delete all these comments after reading them --aidan

            # self.health = min(self.health - (damage_taken - self.resilience), 0)

        # here is my implementation, feel free to change or tweak:

        damage = max(damage_taken - self.stats["resilience"], 0)    # calculate the damage the player should take. maximize to 0 if we have a negative damage value
        print(f"{self.name} takes {damage} damage!")                # tell the user how much damage they took
        self.health -= damage                                       # apply the damage to the player


    def __str__(self):
        """
        returns a string representation of a player instance
        """
        return f"name: {self.name} \nconstitution: {self.stats["constitution"]} \nresilience: {self.stats["resilience"]} \nstrength: {self.stats["strength"]} \nagility: {self.stats["agility"]}"
    