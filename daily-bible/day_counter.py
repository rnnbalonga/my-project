class DayCounter:
    # This class will calculate and track the day the user is in.
    def __init__(self):
        self.day = 0

    def add_day(self):
        self.day += 1
        

test = DayCounter()
print(test.day)
test.add_day()
print(test.day)