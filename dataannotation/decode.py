def decode(message_file):
    # Open and read message file lines
    with open(message_file, "r") as file:
        lines = file.readlines()

    # Create a dictionary mapping index to word
    index_word_map = {int(line.split()[0]): line.split()[1] for line in lines}

    # Initialize the decoded message and counters
    message = []
    line_end = 0
    increment = 1

    # Iterate through the dictionary in a pyramid structure
    # The pyramid structure increases by 1 with each step (like 1, 2, 4, 7, etc.)
    while line_end < len(index_word_map):
        line_end += increment
        message.append(index_word_map[line_end])
        increment += 1
        
    # Join the decoded words into a single string and return
    return " ".join(message)


data = "data.txt"
print(decode(data))
