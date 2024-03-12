class LeftParagraph:
    def __init__(self, len_par):
        self.len_par = len_par
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        len_par = self.len_par
        for _ in range(len(self.words)):
            if len(self.words[_]) <= len_par:
                len_par = len_par - len(self.words[_]) - 1
                print(self.words[_], end=" ")
            else:
                len_par = self.len_par - len(self.words[_]) - 1
                print(end="\n")
                print(self.words[_], end=" ")
        print(end="\n")
        print("----------------------------------------------------------------")
        print()


class RightParagraph:
    def __init__(self, len_par):
        self.len_par = len_par
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):

        for _ in range(len(self.words)):
            if self.words[_] != self.words[-1]:
                if self.len_par <= len(self.words[_]) + 1 + len(self.words[_ + 1]):
                    print(f"{str(self.words[_])} {self.words[_ + 1]}".rjust(self.len_par))
# закончить


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
