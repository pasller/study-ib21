class MinMaxWordFinder:
    def __init__(self):
        self.short_words = []
        self.long_words = []
        self.min_len = 1000
        self.max_len = 0
        self.words = []

    def add_sentence(self, text):
        text = text.lower()
        first_version_words = text.split()
        for word in first_version_words:
            word = str(word).strip(".,/&?")  # убирает знаки припинания
            self.words.append(word)
        print(self.words)

    def shortest_words(self):
        self.min_len = min(len(word) for word in self.words)
        for word in self.words:
            if len(word) == self.min_len:
                self.short_words.append(word)
        self.short_words.sort()
        print(self.short_words)

        return (self.short_words)

    def longest_words(self):
        self.max_len = max(len(word) for word in self.words)
        for word in self.words:
            if (len(word) == self.max_len) and (word not in self.long_words):
                self.long_words.append(word)
        self.long_words.sort()

        return (self.long_words)


# Ваш код
finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('  abc     def    ')
finder.add_sentence('world')
finder.add_sentence('            abc          ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

