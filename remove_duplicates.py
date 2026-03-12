name = "prashnat"
new_name = ""

for i in name:
    if i not in new_name:
        new_name += i
        print("Original:", name)
        print("Updated:", new_name)
