class Rectangle:
    def area(self):
        length = 8
        width = 5
        return length * width


class Triangle:
    def area(self):
        base = 10
        height = 6
        return 0.5 * base * height


def create_shape(shape_name):
    if shape_name.lower() == "rectangle":
        return Rectangle()
    elif shape_name.lower() == "triangle":
        return Triangle()
    else:
        return None


shape1 = create_shape("rectangle")
shape2 = create_shape("triangle")

print("Rectangle Area:", shape1.area())
print("Triangle Area:", shape2.area())

print("\nFactory Pattern executed successfully!")
