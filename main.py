"""
main.py
Author: Dane Rainbird (hello@danerainbird.me)
Purpose: Find any Debug.LogError() calls a given directory of *.cs files and save them to a text file in WikiTable format. 
Last Edited: 02/08/2022
"""

# Imports
import os
import re

'''
Appends the WikiTable header to the Debug.LogError.txt file
'''
def appendWikiTableHeader():
    # Set up DebugLogError.txt to be in the format of a wikitable
    with open("Debug.LogError.txt", "a") as f:
        f.write("{| class=\"wikitable\"\n")
        f.write("! Debug Message !! Function\n")
        f.write("|-\n")
        f.close()

'''
Loops through the directory provided and finds any Debug.LogError() calls
Writes the results to a text file in WikiTable format
'''
def getErrorMessages(dirPath):
    numFiles = numHits = 0
    # Loop through each .cs file in the directory and look for any Debug.LogError() calls
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            if file.endswith(".cs"):
                filePath = os.path.join(root, file)
                numFiles +=1 
                #print("Reading from file: " + filePath) # Debugging / Uncomment if you want to see which file is being read
                with open(filePath, "rb") as f:
                    for line in f:
                        line = line.decode("utf-8")
                        if "Debug.LogError" in line:
                            # Increment hits counter
                            numHits += 1

                            # Find the file name
                            fileName = filePath.split("\\")[-1]

                            # Find the function name
                            functionName = re.search(r'\w+\(', line).group(0)[:-1]

                            # Get the string contained in the Debug.LogError() call (i.e. Debug.LogError("Hello") should return "Hello")
                            # If the Debug.LogError() call does not contain a string, (e.g. it's an object or multiple concatenated variables),
                            # then return [[!TODO - MANUALLY UPDATE]]
                            string = re.search(r'\"[^\"]*\"', line).group(0)[1:-1] if re.search(r'\"[^\"]*\"', line) else "[[!TODO - MANUALLY UPDATE]]"

                            # Write the results to a file
                            with open("Debug.LogError.txt", "a") as f:
                                f.write("| " + string + " || " + fileName + "\n")
                                f.write("|-\n")

                    f.close()
            else:
                continue
        else:
            continue
        break 
    print("Found " + str(numHits) + " hits in " + str(numFiles) + " files")


'''
Appends the WikiTable footer to the Debug.LogError.txt file
'''
def appendWikiTableFooter():
    # Close the wikitable
    with open("Debug.LogError.txt", "a") as f:
        f.write("|}\n")
        f.close()

'''
Initialization / Execution
'''
def init(): 
    # Get the directory path from the user
    dirPath = input("Enter the directory path: ")
    if not os.path.isdir(dirPath):
        print("Invalid directory path")
        exit()
    else:
        appendWikiTableHeader()
        getErrorMessages(dirPath)
        appendWikiTableFooter()
        print("Done!")


if __name__ == "__main__":
    init()
    exit()