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
            data = [line.strip() for line in file]
        return data
    
    def give_line(self, day):
        """
        Give the line that corresponds to the given day.
        """
        line = self.database[day]
        return line
    
    def split_line(self, line):
        """
        Create a list of verses made from give_line method.
        """
        verse = line.split(",")
        return verse

verse = VerseFetcher()
verse_line = verse.give_line(1)
verses = verse.split_line(verse_line)
for verse in verses:
    print(verse)

