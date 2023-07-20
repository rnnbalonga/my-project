path = "D:\workspace\my-project\daily-bible\esv-study-plan\list.txt"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# with open(path, 'r', encoding="utf8") as file:
#     with open("new_list", 'w', encoding="utf8") as new_file:
#         for line in file:
#             line = line.strip()
#             combined_line = ""
#             if not any (word in line for word in months):
#                 combined_line += previous_line + " " + line
#                 line = combined_line
#             previous_line = line
#             new_file.write(line + "\n")

with open("new_list.txt", 'r', encoding="utf8") as file:
    # line_list = file.readlines()
    # for line in line_list:
    #     if line
    pass

def compare_first_15_char(line_1, line_2):
    """
    This function will compare first 15 characters of each line. Return True or False.
    """
    if line_1[0:14] == line_2[0:14]:
        return line_1, line_2
    else:
        return False
    
def compare_str_length(line_1, line_2, lst):
    """
    This function will compare the length of two lines and remove the shorter one from the list.
    """
    new_list = lst
    if len(line_1) >= len(line_2):
        new_list.remove(line_2)
        print(new_list)
    else:
        new_list.remove(line_1)
        print(new_list)
    

#Experiment with variables
sample_line_1 = "Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9,"
sample_line_2 = "Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9, Luke 5:1‐6:16"
sample_line_3 = "Jan 10 Ps 9, Gen 9:20‐10:32, 1 Chr 10,"

# is_same = compare_first_15_char(sample_line_1, sample_line_2)
# is_same_2 = compare_first_15_char(sample_line_1, sample_line_3)
# print(is_same) #True
# print(is_same_2) #False

#Experiment using items in a list
sample_line_list = [sample_line_1, sample_line_2, sample_line_3]
list_is_same = compare_first_15_char(sample_line_list[0], sample_line_list[1])
list_is_same_2 = compare_first_15_char(sample_line_list[0], sample_line_list[2])

compare_str_length(list_is_same[0], list_is_same[1], sample_line_list)
