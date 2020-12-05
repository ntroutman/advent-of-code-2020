def get_input(day, force=False):
    import requests
    import os
    
    full = []
    with open(f"./input/day{day}.txt", "rt") as input_file:
        full = [line.strip() for line in input_file]
            
    example_1 = []
    if os.path.exists(f"./input/day{day}-example1.txt"):
        with open(f"./input/day{day}-example1.txt", "rt") as input_file:
            example_1 = [line.strip() for line in input_file]
            
    example_2 = []
    if os.path.exists(f"./input/day{day}-example2.txt"):
        with open(f"./input/day{day}-example2.txt", "rt") as input_file:
            example_2 = [line.strip() for line in input_file]
    
    return example_1, example_2, full
          