#Open the invited_names text file
with open(r"Input\Names\invited_names.txt") as names:

    #Create a list of names using readlines()
    name_list = names.readlines()

    #Capture each individual name from name_list
    for name_index in range(0, len(name_list) -1):
        name = name_list[name_index]
        
#Use starting_letter.txt
with open("Input\Letters\starting_letter.txt", "r") as letter:
    #Create a list of the lines in text
    letter_line_list = letter.readlines()

    print(letter_line_list[0])
        




#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp