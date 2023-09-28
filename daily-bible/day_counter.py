class DayCounter:
    # This class will calculate and track the day the user is in.
    def __init__(self):
        self.day = 0
        self.path = "last_run_date.txt"

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
    
    def get_origin_date(self):
        """
        Compare origin date with current date
        """
        with open(self.path, 'r', encoding="utf-8") as file:
            last_run_date = file.read()
        
        return last_run_date

    
    def store_date(self, day):
        """
        Store the origin date in the last_run_date.txt file
        """
        with open(self.path, 'w', encoding= "utf-8") as file:
            file.write(day)

    
