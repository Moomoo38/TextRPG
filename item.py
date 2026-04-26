# an example of inheritance
# structuring code via inheritance gives many advantages (organization, code reuse, easier bug fixing)
# i saw the Armor_item class you created, which may cause some problems when we eventually create an inventory
# if we have a bunch of classes like Weapon_item, Armor_item, Potion_item, we will have too many unique classes to account for when storing them in a data structure.
# perhaps we could create an Item class and then have different item classes extend this class!
# here is a basic superclass we can modify that every class that inherits from it will share code with
# go to ArmorItem to see how we inherit, then main file to test
# delete all these comments after you read it --aidan

class Item:
    def __init__(self, name, type):
        """
        initialize an item

        Args:
            name (str): name of the item
            type (str): type of the item
        """
        self.type = type
        self.name = name

    def __str__(self):
        """
        returns a string representation of an item
        """
        return self.name