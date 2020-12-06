import os

def get_input(day, force=False, group_on_blank=False):    
    example_1 = read_file(f"./input/day{day}-example1.txt", group_on_blank)
    example_2 = read_file(f"./input/day{day}-example2.txt", group_on_blank)
    full = read_file(f"./input/day{day}.txt", group_on_blank)
    
    return example_1, example_2, full

def read_file(filename, group_on_blank):
    records = []
    if os.path.exists(filename):
        with open(filename, "rt") as input_file:
            records = [line.strip() for line in input_file]
        
    if group_on_blank:
        groups = [[]]
        for record in records:
            if record == '':
                groups.append([])
                continue
            groups[-1].append(record)
        records = groups
    
    return records

