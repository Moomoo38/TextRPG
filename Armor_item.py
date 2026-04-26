# i will be renaming this class to ArmorItem. it is python convention to name classes like ItemClass, not Item_class
# snake case is primarily use for variable names, function names, and file names
# delete my comments when you finish reading them --aidan

# import the superclass so that we can extend this class from that one
from item import Item

# we can extend a class from another by putting the superclass in parentheses like below
#               VVVV
class ArmorItem(Item):
    #Maybe add armor styles? Heavy medium light ect. 
    #Also considering changing defense and armor to be different, armor being reducing chance to hit on non AP attacks (add tracking attacks for dodge?) and defense being flat reduction in damage

    #Only special or unique items considerable modifiers beyond armor, modifiers can also be negative (such as heavy armor having -agility), obviously most if not all armor types should give resilience
    #Item type is as follows: 1, weapon/shield. 2, helmet. 3, chestplate. 4, leggings/boots. 5, gauntlets.
    def __init__(self, name, armor_type, damage, constitution, resilience, strength, agility):
        """
        initialize an armor item

        Args:
            name (str): the name of the item.
            armor_type (str): armor type (shield, helmet, chestplate, leggings, gauntlets).
            damage (int): not sure what this stat does. is this damage reduction? if so, rename to be more specific.
            constitution (int): constitution modifier the armor gives.
            resilience (int): resilience modifier the armor gives.
            strength (int): strength modifier the armor gives.
            agility (int): agility modifier the armor gives.
        """
        super().__init__(name, "armor")  # initialize the fields in the Item superclass

        # this field you declared is only specific to the ArmorItem class
        self.stats = {
            "armor_type": armor_type,
            "damage": damage,
            "constitution": constitution,
            "resilience": resilience,
            "strength": strength,
            "agility": agility
        }