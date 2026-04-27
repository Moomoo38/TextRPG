# very basic enemy class. remove or change it however you want

class Enemy:
    def __init__(self, name, health):
        """
        initialize an enemy instance

        Args:
            name (str): the name of the enemy
        """
        self.name = name
        self.health = health

    def __str__(self):
        """
        return a string representation of an enemy instance
        """
        return self.name