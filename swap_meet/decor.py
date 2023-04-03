
from swap_meet.item import Item
class Decor(Item):
    def __init__(self, width = 0, length = 0, id = None, condition = 0):
        super().__init__(id = None, condition = 0)
        self.width = width
        self.length = length
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."