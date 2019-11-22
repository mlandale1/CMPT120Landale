# Matt Landale
# Lab 9

    
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def clear(self):
        self.count = 0

    def get_value(self):
        return self.count
    
my_counter = Counter()
my_counter.get_value()
my_counter.increment()
my_counter.increment()
my_counter.get_value()
my_counter.clear()
my_counter.get_value()

