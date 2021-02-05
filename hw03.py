# Problem  A
def anonymize(username, domain):
    '''
    Purpose: To anonymize emails by using astricks.
    Input Parameter(s):
        username - email username of a person
        domain - includes @ and the domain name
    Return Value: Returns the first value of username, 5 astricks, last letter of username, and domain
    '''
    uo=username[0]+"*****"+username[-1]+ domain
    return uo

# #Problem B
def list_swap(vals,idx1,idx2):
     '''
     Purpose: To swap values in the list based on positions of these values.
     Input Parameter(s):
        vals- values in the list
        idx1-  position that swaps with idx2
        idx2-  position that swaps with idx1
     Return Value: new list with swaped values.
     '''
     dep=vals[idx2]
     vals[idx2] = vals[idx1]
     vals[idx1]=dep
     return vals

#Problem C
def codename(first, last, codes):
     '''
     Purpose: To return codename from first and last names.
     Input Parameter(s):
        first- first name
        last- last name
        codes- codes associated with first and last name
     Return Value: code values of first and last name.
     '''
     fir=first[-1]
     las=last[-1]
     codename=codes[fir]+" "+codes[las]
     return codename

# Problem D
def cross(u,v):
     '''
     Purpose: To return the cross product of two vectors.
     Input Parameter(s):
        u- first vectors
        v- second vectors
     Return Value: value of the cross product u x v
     '''
     cp=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
     return cp
