import math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# Example function for background reading

def nickels_to_cents(nickels):
    '''
    Purpose: Converts from a certain number of nickels to
            how many cents we have

    Input Parameter(s):
        nickels: The number of nickels we have

    Return Value:
        the amount of cents we have
    '''
    total = nickels * 5
    return total

# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose: Converts from temperature from a certain celsius to fahrenheit
    Input Parameter(s):
        celsius: Number of celsius given
    Return Value:
        temperature in fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def surface_area_sphere(radius):
    '''
    Purpose: Calculates surface area of sphere given a radius
    Input Parameter(s):
        radius: length of radius
    Return Value:
        surface area of a sphere
    '''
    pi = 3.14159
    rsquared = radius * radius
    area = pi * 4.0 * rsquared
    return area

# Part B: Write out a few simple conversions

def circumference_circle(radius):
    print("TODO: Document and write this function")
    ci=2*math.pi*(radius)
    return ci

def grams_to_ounces(grams):
    print("TODO: Document and write this function")
    oun= grams/28.34952
    return oun

def seconds_to_hours(seconds):
    print("TODO: Document and write this function")
    hou=seconds//360
    return hou

# Part C: Calculate distance based on time and average speed

def calc_distance(minutes, speed):
    print("TODO: Document and write this function")
    hours=minutes/60
    dist=hours*speed
    return dist
