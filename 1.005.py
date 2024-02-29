class BigBell:
    def __init__(self):
        self.times = 0
    def sound(self):
        if self.times % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.times += 1
        



bell = BigBell()
bell.sound()
bell.sound()
bell.sound()