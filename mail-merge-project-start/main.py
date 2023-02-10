#Open the invited_names text file
with open(r"Input\Names\invited_names.txt") as names:
    name_list = names.readlines()
    for name_index in range(0, len(name_list) -1):
        name = name_list[name_index]
        print(name)



#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp