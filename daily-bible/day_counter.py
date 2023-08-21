class DayCounter:
    # This class will calculate and track the day the user is in.
    def __init__(self):
        self.day = 0

    def add_day(self):
        """
        Add +1 to day
        """
        self.day += 1

    def set_day(self, select_day):
        """
        Manually sets the day
        """
        self.day = select_day
        

test = DayCounter()
test.set_day(5)
test.add_day()
print(test.day)