class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return ("{}.{}.{}".format(self.x, self.y, self.z))


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass


block = Block(10, 20, 30)
entity = Entity(50, 60, 70)
thing = Thing(80, 90, 100)

# Получение координат объектов
print("Block coordinates:", block.get_coordinates())
print("Entity coordinates:", entity.get_coordinates())
print("Thing coordinates:", thing.get_coordinates())

# Перемещение сущности
entity.move(55, 65, 75)
print("Entity new coordinates:", entity.get_coordinates())

# Разрушение блока
block.shatter()
print("Block after shattering:", block.get_coordinates())
