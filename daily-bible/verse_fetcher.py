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
    
    def create_verse_line(self, line):
        """
        Create a list of verses made from give_line method.
        """
        verse = line.split(",")
        return verse
    
    def clean_verse_line(self, verse_list):
        """
        This is the final method.
        """  
        for i in range(len(verse_list)) :
            if verse_list[i][0] == " ":
                clean_verse = verse_list[i].lstrip()
                verse_list[i] = clean_verse
            else:
                pass
        print(verse_list) 




verse = VerseFetcher()
verse_line = ['Ps 1', ' Gen 2', ' 1 Chr 2', ' Luke 1:26‐56']

# for verse in verse_line:
#     if verse[0] == " ":
#         new = verse.lstrip()
#         print(new)
#     else:
#         print(verse)
    
# for i in range(len(verse_line)):
#     if verse_line[i][0] == " ":
#         new = verse_line[i].lstrip()
#         verse_line[i] = new
#     else:
#         pass

verse.clean_verse_line(verse_line)



