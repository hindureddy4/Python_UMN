import random
# Problem A: six_tails
def six_tails():
    '''
    Purpose: To count how many times a coin needs to be flipped until you get six tails in a row
    Input Parameter(s): None
    Return value: Number of times a coin needs to be flipped until you get 6 tails in a row
    '''
    i=0
    counter=0
    while i<6:
        rand=random.randint(0,1)
        if rand==0:
            i=i+1
        else:
            i=0
        counter=counter+1
    return counter



# Problem B: average_six
def average_six(n):
    '''
    Purpose: To calculate the average of results from six_tails()
    Input Parameter(s): N : number of times the loop should run
    Return value: Average of results
    '''
    tot=0
    for i in range(n):
        t=six_tails()
        tot=tot+t
    return (tot/n)


# Problem C: population
def population(small, middle, big):
    '''
    Purpose: Simulate the populations of three types of fish living in an isolated lake
    Input Parameter(s): small: number of small fish
    middle: number of middle fish
    big:number of big fish
    Return value: number of weeks it takes for population to be wiped out.
    '''
    week=0
    while (small>=10 and middle>=10 and big>=10 and week<30) :
        new_small = int(1.1*small - 0.0002*small*middle)
        new_middle = int(0.95*middle + 0.0001*small*middle - 0.00025*middle*big)
        new_big = int(0.9*big + 0.0002*middle*big)
        small=new_small
        middle=new_middle
        big=new_big
        week=week+1
        print("Week",week,"- Small:",small," Middle:",middle,"Big:",big)
    return week

# Problem D: find_password
def find_password(filename):
    '''
    Purpose:
      Given an encrypted file, tries every possible four letter lowercase
      password for that file until one works, and then returns the password.
    Input Parameter(s):
      filename is a string representing the name of the encrypted file.
      The file must be in the same folder as this script.
    Return Value:
      Returns the password that successfully decrypts the given file
    '''
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'

    passt=0
    for one in range(97,123):
        for two in range(97,123):
            for three in range(97,123):
                for four in range(97,123):
                    password=chr(one)+chr(two)+chr(three)+chr(four)
                    if decrypt(data,password):
                        passt=1
                        return password
    if(passt==0):
        return False

#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

def decrypt(data, password):
    '''
    Purpose:
      Check whether the password is correct for a given encrypted
      file, and print out the decrypted contents if it is.
    Input Parameter(s):
      data is a string, representing the contents of an encrypted file.
      password is a four letter lowercase string, representing the password
      used to encrypt/decrypt the file contents.
    Return Value:
      Returns True if the password is correct and the file contents
      were printed.  Returns False and prints nothing otherwise.
    '''
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

def encode(key):
    '''
    Purpose:
      Turn a password into a ~9 digit number
    Input Parameter(s):
      key is a four letter string representing a password
    Return Value:
      Returns a number between 0 and 547120140, using modular exponentiation
      to make it difficult to reverse engineer the password from the number.
    '''
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

def vigenere(msg,key):
    '''
    Purpose:
      Decipher a message using the Vigenere cipher
    Input Parameter(s):
      msg a string, representing the encrypted message
      key is a four letter string, representing the cipher key
    Return Value:
      Returns a string representing the deciphered text
    '''
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')
