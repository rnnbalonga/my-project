path = "D:\workspace\my-project\daily-bible\esv-study-plan\list.txt"

with open(path, 'r', encoding="utf8") as file:
    for line in file:
        print(line.strip())  # Use t