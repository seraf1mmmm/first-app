class Poweroftwo:
    def __init__(self):
        self.exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = 2 ** self.exponent
        self.exponent += 1
        return result

io = int(input("How many?: "))

powers = Poweroftwo()
for _ in range(io):
    print(next(powers))