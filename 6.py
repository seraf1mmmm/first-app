class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number


    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


count = Counter(10)
for elem in count:
    print(elem)



def raise_to_the_degrees(number, max_degrees):
    i = 0
    while True:
        result = number**i
        yield result
        if result>100**20:
            return
        i+=1

res = raise_to_the_degrees(122345, 500)
print(res)
for _ in res:
    print(_)