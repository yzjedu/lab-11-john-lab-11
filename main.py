# John Elehwany
# Loyola CS151, Lab 11
# Professor Zee
# Due Date: November 26, 2024

# Converts a file of Morse code translations into a dictionary.
# Name: morse_to_dictionary
# Parameters: file_name
# Return: dictionary
def morse_to_dictionary(file_name):
    morse_dict = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if '\t' in line:
                    morse, letter = line.strip().split('\t')
                    morse_dict[morse] = letter
    except FileNotFoundError:
        print("Error: File not found.")
    return morse_dict


# Reads the input Morse code file and checks if it exists.
# Name: read_morse_file
# Parameters: None
# Return: file_name
def morse_to_dictionary(file_name):
    morse_dict = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if '\t' in line:
                    parts = line.split('\t')
                    if len(parts) == 2:
                        morse, letter = parts
                        morse_dict[morse] = letter
    except FileNotFoundError:
        print("Error: The file was not found")
    return morse_dict


# Translates a list of Morse code lines into English using a dictionary.
# Name: convert_morse_to_english
# Parameters: morse_lines (list), morse_dict (dictionary)
# Return: translated_lines (list)
def convert_morse_to_english(morse_lines, morse_dict):
    translated_lines = []
    for line in morse_lines:
        symbols = line.split()
        word = ""
        for symbol in symbols:
            if symbol in morse_dict:
                word += morse_dict[symbol]
            else:
                word += "?"
        translated_lines.append(word)
    return translated_lines

# Writes translated English sentences to an output file.
# Name: write_english_file
# Parameters: file_name (string), translated_lines (list)
# Return: None
def write_english_file(file_name, translated_lines):
    file = open(file_name, 'w')
    for line in translated_lines:
        file.write(line + '\n')
    file.close()
    print("Translated Morse code saved to", file_name)

# Purpose: Main function. Calls all functions above.
# Name: main
# Parameters: None
# Return: None
def main():
    dictionary_file = input("Enter the name of the Morse code dictionary file: ")
    morse_dict = morse_to_dictionary(dictionary_file)
    if not morse_dict:
        return

    morse_file_name = read_morse_file()
    file = open(morse_file_name, 'r')
    morse_lines = []
    for line in file:
        morse_lines.append(line.strip())
    file.close()

    translated_lines = convert_morse_to_english(morse_lines, morse_dict)
    output_file_name = input("Enter the name of the output file: ")
    write_english_file(output_file_name, translated_lines)

    print("Morse code translation complete!")


main()
