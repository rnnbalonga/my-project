path = "D:\workspace\my-project\daily-bible\esv-study-plan\list.txt"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


with open(path, 'r', encoding="utf8") as file:
    for line in file:
        line = line.strip()
        combined_line = ""
        if not any (word in line for word in months):
            combined_line += previous_line + " " + line
            print(combined_line)
        previous_line = line