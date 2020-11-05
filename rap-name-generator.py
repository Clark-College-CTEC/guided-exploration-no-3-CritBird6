# Guided Exploration No. 3
# Rhaevyn Lindsay

# importing the random libary form python
import random


def main():
    # the variable where we will be storing user input in the form of a list
    possible_names = []
    # the file that will be storing the data we accumulate
    outputFile = open('rap-names-output.txt', 'w')

    # We are establishing that with our rap file we are going to do the stuff later stated
    with open('rap-names.txt', 'r') as dataFile:
        # we are saying that for every name in the file the loop will strip on the right side of name
        for name in dataFile:
            # here we are appending names to our possible names list and getting rid of extra space
            possible_names.append(name.rstrip())

     # our count variable will take the user input of how many names they want to make
    count = int(input('How many rap names would you like to create? '))
    # our variable will store the user input of how many parts should be in the name
    parts = int(input('How many parts should the name contain? '))
    # the for loop will take the amount put in the count variable and loop that many times
    for i in range(count):
        # for each time the loop starts we'll add how many parts they wanted.
        name_parts = []
    # our loop here will loop how many names the user thought should contain
        for j in range(parts):
            # the loop will then add random selections and creations of the names to name_parts variable
            name_parts.append(
                possible_names[random.randint(0, len(possible_names)-1)])
        # here we are writing on our outputfile in one line the names that we accumulated in the two previous loops
        outputFile.write(f"{' '.join(name_parts)}\n")
        # here we are printing the name(s) the program came up with
        print(f"{' '.join(name_parts)}")
        # our program is done so we are officially closing it.
        outputFile.close()


main()
