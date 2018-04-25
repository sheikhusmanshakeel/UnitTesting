from drawing_helper.shape_draw_helper import can_draw, draw_shape


class Square:
    def __init__(self, id, side):
        self.id = id
        self.side = side
        self.name = "Square"
        self.can_be_drawn = can_draw(self)

    def is_closed(self):
        if self.name.lower() in ["circle", "triangle", "rectangle", "square"]:
            return True
        else:
            return False

    def calculate_area(self):
        return self.side * self.side

    def draw(self):
        if self.can_be_drawn:
            draw_shape(self)
        else:
            print("This shape can't be drawn")

    def send_shape(self, send_shape_to_people):
        send_shape_to_people.send(self.name)


class Rhombus:
    def __init__(self, id, height, width):
        self.id = id
        self.name = "rhombus"
        self.height = height
        self.width = width
        self.can_be_drawn = can_draw(self)

    def is_closed(self):
        return False

    def calculate_area(self):
        return (self.height * self.width) / 2

    def draw(self):
        if self.can_be_drawn:
            draw_shape(self)
        else:
            print("This shape can't be drawn")

    def send_shape(self, send_shape_to_people):
        send_shape_to_people.send(self.name)
