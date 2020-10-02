bot_fav_color = "blue"
# Creating a parent class to use for various games


class Player:
    def __init__(self, name, fav_color, ab):
        self.name = name
        self.fav_color = fav_color
        self.ab = ab

    def __str__(self):
        if self.fav_color == "blue":
            return f"Hi {self.name}! My favorite color is also blue!"
        return f"Hi {self.name}! {self.fav_color} is an awesome color!"


# Forming a repeatable stack structure
class Stack:
    def __init__(self, abc):
        self.height = 4
        self.abc = abc

    def move_piece(self):
        self.height -= 1


# To give the player 3 stacks of 4 pieces and identify whether they are playing as white or black
class GobletPlayer(Player):
    def __init__(self, name, fav_color, ab, wb):
        self.color = wb
        self.stack_a = Stack(ab + 'a')
        self.stack_b = Stack(ab + 'b')
        self.stack_c = Stack(ab + 'c')
        super.__init__(name, fav_color, ab)
