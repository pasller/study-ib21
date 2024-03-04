class BoundingRectangle:
    def __init__(self):
        self.all_point = []
        self.count_point = 0
        self.all_point.append([0, 0])
        self.x_point = []
        self.y_point = []

    def add_point(self, x, y):
        self.count_point += 1
        self.all_point.append([x, y])
        for _ in range(len(self.all_point)):
            for __ in range(2):
                if __ == 0:
                    self.x_point.append((self.all_point[_])[__])
                else:
                    self.y_point.append((self.all_point[_])[__])
        self.max_x = max(self.x_point)
        self.min_x = min(self.x_point)

        self.max_y = max(self.y_point)
        self.min_y = min(self.y_point)

    def width(self):

        return ("ширина прямоугольника = ", self.max_x - self.min_x)

    def height(self):
        return ("высота прямоугольника = ", self.max_y - self.min_y)

    def bottom_y(self):
        return ("координата нижней границы прямоугольника = ", self.min_y)

    def top_y(self):
        return ("координата верхней гранциы прямоугольника = ", self.max_y)

    def left_x(self):
        return ("координата левой границы прямоугольника = ", self.min_x)

    def right_x(self):
        return ("координата правой границы прямоугольника = ", self.max_x)


# Ваш код

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())