#!/usr/bin/python

"""
Temperature conversion program used to demonstrate:

* interactive programs
* data types
* basic computation

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

def main():
    
    # Print program name
    print("Farenheight to Celsius converter", end = "\n\n")


    # Request user input
    temp_f = input("Enter the Tempreture(without units): ")
    print(temp_f)

    # Perform calculation
    temp_c =int(temp_f) - 32
    temp_c *= 5/9
    
    

    # Report result
    print("The Tempreture is: ", temp_c)

if __name__ == "__main__":
    main()
