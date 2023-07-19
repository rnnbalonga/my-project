path = "D:\workspace\my-project\daily-bible\esv-study-plan\list.txt"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


with open(path, 'r', encoding="utf8") as file:
    with open("new_list", 'w', encoding="utf8") as new_file:
        for line in file:
            line = line.strip()
            combined_line = ""
            if not any (word in line for word in months):
                combined_line += previous_line + " " + line
                line = combined_line
            previous_line = line
            new_file.write(line + "\n")