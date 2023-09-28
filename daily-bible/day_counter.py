class DayCounter:
    # This class will calculate and track the day the user is in.
    def __init__(self):
        self.day = 0
        self.origin_date = self.get_origin_date("last_run_date.txt")

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
    
    def get_origin_date(self, path):
        """
        Compare origin date with current date
        """
        with open(path, 'r', encoding="utf-8") as file:
            last_run_date = file.readline
        
        return last_run_date
        
    
    def store_date(self, day, path):
        """
        Store the origin date in the last_run_date.txt file
        """
        with open(path, 'w', encoding= "utf-8") as file:
            file.write(day)

from datetime import date

user_day = DayCounter()

current_date = str(date.today())

if user_day.compare_date(current_date):
    print("SONO MAMA")
else:
    print("OH WELL")
# origin_date = user_day.origin_date

# if current_date != origin_date:
#     origin_date = current_date
#     user_day.add_day()


