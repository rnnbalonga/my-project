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
    
    def print_day(self):
        """
        Prints the current day of the plan.
        """
        print(f"You are at day {self.day} of the study plan.")

test = DayCounter()
test.set_day(5)
test.add_day()
test.print_day()