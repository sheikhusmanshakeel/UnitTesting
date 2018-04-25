def draw_shape(shape_object):
    print("I draw shape of type {0}".format(shape_object.name))


def can_draw(shape_object):
    if shape_object.name in ["square", "rectangle"]:
        return True
    else:
        return False


class SendShapeToPeople:
    def send(self, name):
        print("I have sent {0} to all the people on the plant.".format(name))
