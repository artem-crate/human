class IterableGenerator:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for item in self.iterable:
            yield item

my_list = [1, 2, 3, 4, 5]
iterable_generator = IterableGenerator(my_list)

for item in iterable_generator:
    print(item)