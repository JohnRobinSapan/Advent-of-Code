data = "data.txt"


def decode(message_file):
    # Open the message file
    with open(message_file, "r") as file:
        # Read all lines from the file
        lines = file.readlines()

        # Create a dictionary mapping numbers to words from the lines
        message_dict = {int(line.split()[0]): line.split()[1] for line in lines}

        # Calculate the height of the pyramid based on the number of lines
        pyramid_height = int((-1 + (1 + 8 * len(lines)) ** 0.5) / 2)

        # Calculate the numbers at the end of each line of the pyramid
        pyramid_endings = [int((n * (n + 1)) / 2) for n in range(1, pyramid_height + 1)]

        # Construct the decoded message by retrieving words from the dictionary
        message = " ".join([message_dict[i] for i in pyramid_endings])

    return message





print(decode(data))
