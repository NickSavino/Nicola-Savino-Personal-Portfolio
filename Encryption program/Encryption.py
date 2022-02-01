# encryption.py
# Nicola Savino, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.



### Define your functions here


def take_user_input():
    '''This function takes user input to decide whether to encode or decode their text/cypher
    
    Paramaters: None

    Returns: None
    
    '''
    selection = int(input('Select 1 to encode, 2 to decode, or 0 to quit: '))       #takes menu selection as an integer
    if selection == 0:                                                              #if statement that quits program on user selection
        quit()
    
    cypher = str(input('Please enter your 26 character alphanumeric cipher: '))     #takes cypher as a string
    cypher.split()                                                                  #splits each caharacter of cypher
    cypher = check_cypher_validity(cypher)
    
    text = str(input('Please enter your text you wish to encode/decode: '))         #takes text as a string
    #the following if block decides on wether to encode or decode the text based on user selection
    if selection == 1:                                                         
        encode_text(cypher, text)
    elif selection == 2:
        decode_text(cypher, text)
    return selection, cypher, text


def check_cypher_validity(cypher):
    '''checks for validity of user created cypher
    
    Parameters: cypher

    Returns: cypher_valid
    
    '''
    cypher_valid = True                                 #initializes boolean to check if cypher is valid
    if (cypher.isalnum() == False) or (len(cypher) < 26): #if the cypher is not alphanumeric or less than 26 characters in length, take user input again.
        print("Cypher Invalid\nPlease Retry")
        take_user_input()
    if cypher.islower() == False:                     #if not every index in cypher is lowercase, convert to lowercase
        print('Uppercase characters found, converting to lowercase...')
        cypher = cypher.lower()
        print(cypher)
    if len(cypher) > 26:
        cypher = remove_duplicates(cypher)              #reassigns cypher as the same cypher but with duplicates removed
        if len(cypher) > 26:                            #if the cypher is still greater than 26 characters after duplicate removal, prompt user input
            print("Removed Duplicates, cypher is still too long\nPlease Retry")
            take_user_input()                           #loops program if cypher is invalid
            
    if cypher_valid == True:                            #checks if boolean for cypher validity is true, printing if yes
        print('Cypher {} is valid'.format(cypher))
        return cypher

def remove_duplicates(arr):
    '''Removes duplicates of the cypher if it contains more than 26 characters

    Parameters: arr

    Returns: temp

    '''
    temp = ""
    for i in range(0, len(arr)):                          #for loop that executes once for every character in the list      
        if temp.count(arr[i]) == 0:                       #if the value that temp is counting hasn't appeared yet, add to list.
            temp += arr[i]
    if temp != arr:
        print('Duplicates found in cypher, removing...')
    return temp                                           #return list without duplicates

def encode_text(cypher, text):
    '''Encodes text on user selection
    
    Parameters: cypher_dict, text

    Returns: None

    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher_dict = dict(zip(alphabet, cypher))          #maps each character of the cypher to a Key as a Value
    encrypted_text = []                                     #new list object for encrypted text
    for i in range(len(text)):                            #appends each characters corresponding cypher value to the encrypted text list
        encrypted_text.append(cypher_dict.get(text[i]))
    encrypted_text = ''.join(encrypted_text)                #converts the encrypted text into a list and prints NOTE Currently does not work with spaces         
    print('Your output is:', encrypted_text)                #prints encrypted text
    take_user_input()                                       #loops program

def decode_text(cypher_dict, text):
    '''Decodes text on user selection, effectively reverse operation of encode_text() function
    
    Parameters: cypher_dict, text

    Returns: None
    
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher_dict = dict(zip(cypher_dict, alphabet))          #maps each character of the alphabet to a Key as a Value 
    decrypted_text = []                                     #new list object for encrypted text
    for i in range(len(text)):                            #appends each characters corresponding cypher value to the encrypted text list
        decrypted_text.append(cypher_dict.get(text[i]))
    decrypted_text = ''.join(decrypted_text)                #converts the encrypted text into a list and prints         
    print('Your output is:', decrypted_text)                #prints encrypted text
    take_user_input()                                       #loops program


def quit():
    '''Called whenever program needs to be terminated
    
    Parameters: None

    Returns: None

    '''
    print('Thank you for using the encryption program.')
    exit()                                                  #built in function that quits program


def main():
    '''Main function of program
    
    Parameters: None

    Returns: None

    '''
    print("ENDG 233 Encryption Program")                    #welcome title
    take_user_input()                                       #calls for user input function    


main()  #Main Program


