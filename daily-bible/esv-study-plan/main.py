def compare_first_15_char(prev_line, current_line):
    """
    This function will compare first 15 characters of each line. Return True or False.
    """
    if current_line[0:14] == prev_line[0:14]:
        return True
    else:
        return False
    
def compare_str_length(prev_line, current_line):
    """
    This function will compare the length of two lines.
    """
    if len(current_line) > len(prev_line):
        return current_line
    else:
        return prev_line

def remove_first_two_words(line):
    """
    Remove first two words separated by " " in each line.
    """
    new_line = ' '.join(line.split()[2:])
    return new_line

with open("new_list.txt", 'r', encoding="utf8") as file:
    line_list = file.readlines()
    raw_list = []
    for i in range(len(line_list)):
        line = remove_first_two_words(line_list[i].strip())
        raw_list.append(line)
    # print(len(raw_list))

file.close()
        
clean_list = []

for i in range(0, len(raw_list)):
    if i == 0:
        clean_list.append(raw_list[i])
        # print(clean_list)
    else:
        prev_line = clean_list[-1]
        current_line = raw_list[i]

        is_same = compare_first_15_char(prev_line, current_line)

        if is_same:
            longer_line = compare_str_length(prev_line, current_line)
            prev_line = longer_line
        
        else:
            clean_list.append(current_line)

print(clean_list[0])

# with open("clean_list.txt", "w", encoding="utf-8") as clean_file:
#     for i in range(0, len(clean_list)):   
#         clean_file.write(f'{clean_list[i]} \n')

# clean_file.close()



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

