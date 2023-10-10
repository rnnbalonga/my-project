class VerseFetcher:
    # The aim for this class is to generate all the verses needed for a specific day.
    # Day Counter is not part of this class but would be provided through another class.

    def __init__(self):
        self.database = self.read_data("esv-study-plan\clean_list.txt")

    def read_data(self, path):
        """
        Fetch the items from clean_list.
        """
        with open (path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    
    def give_line(self, day):
        return self.database[day]
    
    def create_verse_line(self, line):
        return line.split(",")
    
    def clean_verse_line(self, verse_list):
        """
        Remove leading whitespace from verses.
        """  
        for i in range(len(verse_list)) :
            if verse_list[i][0] == " ":
                clean_verse = verse_list[i].lstrip()
                verse_list[i] = clean_verse

        return verse_list
    
    def daily_verse(self, day):
        """
        Final method to give verses for the day. Day of the year (integer from 0-364) is needed as input. Output will be a list of verses.
        """
        raw_line = self.give_line(day)
        verse_line = self.create_verse_line(raw_line)
        clean_verse_line = self.clean_verse_line(verse_line)

        return clean_verse_line

