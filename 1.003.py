class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, Rweight):
        self.right += Rweight

    def add_left(self, Lweight):
        self.left += Lweight

    def result(self):
        if self.right > self.left:
            return("R")
        elif self.right == self.left:
            return("=")
        elif self.right < self.left:
            return("L")

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
