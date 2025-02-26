from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, type = "Unknown", id = None, condition = 0, age = 0):
        super().__init__(condition, id, age)
        self.type = type

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
