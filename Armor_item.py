class Armor_item:
    #Maybe add armor styles? Heavy medium light ect. 
    #Also considering changing defense and armor to be different, armor being reducing chance to hit on non AP attacks (add tracking attacks for dodge?) and defense being flat reduction in damage

    #Only special or unique items considerable modifiers beyond armor, modifiers can also be negative (such as heavy armor having -agility), obviously most if not all armor types should give resilience
    #Item type is as follows: 1, weapon/shield. 2, helmet. 3, chestplate. 4, leggings/boots. 5, gauntlets.
    def __init__(self, item_type, damage, constitution, resilience, strength, agility):
        self.stats = {
            "item_type": item_type,
            "damage": damage,
            "constitution": constitution,
            "resilience": resilience,
            "strength": strength,
            "agility": agility
        }