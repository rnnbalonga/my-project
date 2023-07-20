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


sample_line_1 = "Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9,"
sample_line_2 = "Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9, Luke 5:1‐6:16"



def compare_first_15_char(line_1, line_2):
    """
    This function will compare first 15 characters of each line. Return True or False.
    """
    if line_1[0:14] == line_2[0:14]:
        return True
    else:
        return False
    
is_same = compare_first_15_char(sample_line_1, sample_line_2)
print(is_same)