def decode(message_file):
    with open(message_file, "r") as f:
        lines = f.readlines()
    # Initialize an empty list to store the message words
    message_words = []

    # Store a null length placeholder in each list element
    for x in range(3):
        message_words.append('')

    # Loop through the lines
    for line in lines:
        # Split the line by space and get the first element as the number
        number = int(line.split()[0])

        # Determine if the number equates to the last element value of a "pyramid" line
        for x in range(3):
            if number == (int((x * x + x)/2)):
                message_words[x] = line.split()[1]
                break

    # Now, concatenate the non-null list values together to form a sentence.
    text = ""

    for x in message_words:
        if x != '':
            text = text + x + " "

    # Return the result
    return text

print(decode(r'C:\Users\Haarisah Hussain\Documents\Decoding\PythonApplication1\coding_qual_input.txt'))