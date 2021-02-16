#Problem A


'''
Purpose: To calculate the amount of Tax owed.
Input Parameter(s):
    married: Defines if the person is single or married
    taxable_income: The income of the person or couple in the previous year
Return Value: The return value is the amount of tax owed by the person or a married couple
'''
def compute_tax(married, taxable_income):
    if married==False:
        if taxable_income<40000:
            tax= taxable_income*0.1
        elif taxable_income<160000:
            tax=4000 +(taxable_income-40000)*0.2
        elif taxable_income>=160000:
            tax=28000+(taxable_income-160000)*0.3
    elif married==True:
        if taxable_income<80000:
            tax= taxable_income*0.1
        elif taxable_income<320000:
            tax=8000 +(taxable_income-80000)*0.2
        elif taxable_income>=320000:
            tax=56000+(taxable_income-320000)*0.3
    else:
        print("error")
    return round(tax,2)


#Problem B



def choice(text, optionA, optionB, optionC):
    '''
    Purpose: Choose an option from the given input
    Input Parameter(s):
    text: First statement printed
    optionA: one choice
    optionB: second choice
    optionC: third choice
    Return Value: option that was chosen will be returned
    '''
    print(text)
    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)
    io=input("Choose A, B, or C:")
    if io=='A' or io=='B' or io=='C':
        return io
    else:
        print("Invalid option, defaulting to A")
        return 'A'


#Problem C

def adventure():
    '''
    Purpose: creating a game which could have several endings
    Input Parameter(s): none specified, but could take in multiple commands
    Return Value: True or False based on the game's success
    '''
    io=choice("no 1","1","2","3")

    if(io=="A"):
        io=choice("no 2","1","2","3")
        if(io=='A'):
            return True
        elif(io=="B"):
            io=choice("no 4","1","2","3")
            if(io=="A" or io=="B"):
                return True
            else:
                return False
        else:
            io=choice("no 3","1","2","3")
            if(io=="A"):
                return False
            elif(io=="C"):
                return True
            else:
                io=choice("no 4","1","2","3")
                if(io=="A" or io=="B"):
                    return True
                else:
                    return False
    elif(io=="C"):
        io=choice("no 3","1","2","3")
        if(io=="A"):
            return False
        elif(io=="C"):
            return True
        else:
            io=choice("no 4","1","2","3")
            if(io=="A" or io=="B"):
                return True
    else:
        return False
