# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее арифметическое
# последовательности целых чисел. Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять
# в статистику число, которое будет учтено при вычислении финального результата методом result. Для экземпляров MinStat
# и MaxStat result должен возвращать целое число, для AverageStat — число типа float (это число будет сравниваться с
# правильным ответом до седьмой значащей цифры). Если в последовательности отсутствуют числа и статистические величины
# вычислить невозможно, метод result должен возвращать None.

class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        return (min(self.numbers))


class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        return (max(self.numbers))


class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        avg = float
        summ = sum(self.numbers)
        avg = summ / len(self.numbers)
        return (avg)


# Ваш код

values = [1, 2, 4, 4]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
