# Import sys to redirect input and output
import sys
from os import makedirs
from os.path import exists

# Take input of number of testfiles and folder path
folderPath = input('Enter the relative folder path: ')
testFiles= int(input('Enter the number of test files: '))

# Create a new input and output file for each test file
for i in range(testFiles):
    # Create a new input and output directory if they don't exist
    if not exists(f'{folderPath}/input'):
        makedirs(f'{folderPath}/input')
    if not exists(f'{folderPath}/output'):
        makedirs(f'{folderPath}/output')

    # Open the input and output file
    inputFile = None
    outputFile = None
    try:
        inputFile = open(f'{folderPath}/input/{i}.in', 'w')
        outputFile = open(f'{folderPath}/output/{i}.in', 'w')
    except:
        print('Error opening the files')
        continue

    # Write the data to the input file
    sys.stdout = inputFile
    with open(f'{folderPath}/Generator.py', 'r', encoding = 'utf8') as generatorFile:
        exec(generatorFile.read())

    # Write the result to the output file
    sys.stdin = inputFile
    sys.stdout = outputFile
    with open(f'{folderPath}/Solution.py', 'r', encoding = 'utf8') as solutionFile:
        exec(solutionFile.read())
    
    # Close the files
    inputFile.close()
    outputFile.close()