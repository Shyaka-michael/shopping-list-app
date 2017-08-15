"""
module for item class
"""
class Item:

    """
     item class which creates item
    """
    def __init__(self, name, quantity):
        """
        initial method which sets name and quantity for item
        """
        self.name = name
        self.quantity = quantity
