class DayCounter:
    # This class will calculate and track the day the user is in.
    def __init__(self):
        self.day = 0
        self.origin_date = ""

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
        print(f"You are at ay {self.day} of the study plan.")

