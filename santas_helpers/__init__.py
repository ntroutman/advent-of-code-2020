def get_advent_input(day, force=False):
    import requests
    import os
    
    input_filename = f"./day{day}/input.txt"
    
    if os.path.exists(input_filename):
        with open(input_filename, "rt") as input_file:
            return [line.strip() for line in input_file]
    
    # this doesn't work because of a 400 error .... figure it out later
    with open(input_filename, "wb") as input_file:
        response = requests.get(f"https://adventofcode.com/2020/day/{day}/input")
        content = response.content
        input_file.write(content)
        return content.decode('utf-8')