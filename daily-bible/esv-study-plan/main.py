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
    if len(line_1) >= len(line_2):
        lst.remove(line_2)
        # print(lst)
    else:
        lst.remove(line_1)
        # print(lst)

with open("new_list.txt", 'r', encoding="utf8") as file:
    line_list = file.readlines()
    clean_list = []
    #Create clean list
    for i in range(len(line_list)):
        line = line_list[i].strip()
        clean_list.append(line)

    
    #Use the two functions to reduce lines in clean_list
    # for i in range(0,10):
    #         line_1 = clean_list[i]
    #         line_2 = clean_list[i+1]
    #         is_same_15_char = compare_first_15_char(line_1, line_2)
    #         if not is_same_15_char:
    #             compare_str_length(line_1, line_2, clean_list)

    print(len(clean_list))
    print(clean_list[550])
### CODE FOR FORMATTING (NOT NEEDED) ###

# path = "D:\workspace\my-project\daily-bible\esv-study-plan\list.txt"

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


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

### TESTS ###

# #Experiment with variables
# sample_line_list = ["Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9,", "Jan 9 Ps 8, Gen 8:20‐9:19, 1 Chr 9, Luke 5:1‐6:16", "BROOOOOO"]

# is_same = compare_first_15_char(sample_line_1, sample_line_2)
# is_same_2 = compare_first_15_char(sample_line_1, sample_line_3)
# print(is_same) #True
# print(is_same_2) #False

#Experiment using items in a list
# list_is_same = compare_first_15_char(sample_line_list[0], sample_line_list[1])
# list_is_same_2 = compare_first_15_char(sample_line_list[0], sample_line_list[2])

# if list_is_same:
#     compare_str_length(list_is_same[0], list_is_same[1], sample_line_list)

