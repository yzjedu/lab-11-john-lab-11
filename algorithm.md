# Algorithm Document

- John Elehwany
- CS 151 Lab 11
- Professor Zee
- Due November 26, 2024

This code converts documents written in morse code into a document written in plain English via a morse code translation sheet.
1. Ask user for input file name
2. Ask user for output file name
3. Use try/except to see if the file exists  


- Purpose: Converts the morsecode.txt file into a dictionary
- Name: morse_to_dictionary
- Parameters: file_name  
- Return: dictionary
1. Open morsecode.txt (reading)
2. Create an empty dictionary to store Morse code and its corresponding English letter
3. Read each line from the file
4. Split each line by tab (\t) to separate the Morse code from the English letter
5. Strip any extra spaces from the Morse code and the English letter
6. Store the Morse code as the key and the letter as the value in the dictionary
7. Return dictionary



- Purpose: Reads the input morse code file
- Name: read_morse_file  
- Parameters: file_name  
- Return: file_name (string)
1. Loop for file name input 
2. Use try and except for file checking
3. It file doesn't open, output error message
4. If file exists, return file_name


- Purpose: Translates a list of Morse code into English using a dictionary  
- Name: convert_morse_to_english  
- Parameters: morse_lines (list), morse_dict (dictionary)  
- Return: translated_lines (list)
1. Create an empty list (for Morse)
2. Loop through each line in the list
3. Split the line into symbols using spaces 
4. For each symbol, translate into a letter via dictionary
5. Combine all letters into a sentence and add it to list
6. Return list


- Purpose: Writes the translated English sentences to an output file  
- Name: write_english_file
- Parameters: file_name (string), translated_lines (list)  
- Return: None
1. Open chosen output file for writing
2. Loop through the list of translated sentences
3. Write each sentence to the file followed by a newline
4. Close file

- Purpose: Main function. Calls all functions above
- Name: main
- Parameters: None  
- Return: None
1. Ask for input of name of dictionary file
2. Load dictionary via morse_to_dictionary
3. Ask for input of morse code file name
4. Ask for input of output file name
5. Use convert_morse_to_english to convert selected file 
6. Use write_english_file to put converted results onto
7. Print success message
---

1. Run main()