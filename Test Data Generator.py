# Import sys to redirect input and output
import sys
from os import makedirs
from os.path import exists
from importlib.util import spec_from_file_location, module_from_spec

# Take input of number of testfiles and folder path
folderPath = input('Enter the relative folder path: ').strip()

# Get subtask distribution
with open(f'{folderPath}/Subtasks.txt') as subtasksFile:
    subtasks = list(map(int, subtasksFile.read().split()))

# Create a new input and output file for each test file
for testFileCount, subtask in enumerate(subtasks):
    testFile = testFileCount + 1

    # Create a new input and output directory if they don't exist
    if not exists(f'{folderPath}/input'):
        makedirs(f'{folderPath}/input')
    if not exists(f'{folderPath}/output'):
        makedirs(f'{folderPath}/output')

    # Open the input and output file
    inputFile = None
    outputFile = None
    try:
        inputFile = open(f'{folderPath}/input/input0{testFile}.txt', 'w')
        outputFile = open(f'{folderPath}/output/output0{testFile}.txt', 'w')
    except:
        print('Error opening the files')
        continue

    # Check if files exist
    if exists(f'{folderPath}/Generator.py'):
        # Write the data to the input file
        sys.stdout = inputFile
        spec = spec_from_file_location('Generator', f'{folderPath}/Generator.py')
        generatorModule = module_from_spec(spec)
        spec.loader.exec_module(generatorModule)
        generatorModule.generate(subtask)

    # Open the input file in read mode
    try:
        inputFile = open(f'{folderPath}/input/input0{testFile}.txt', 'r')
    except:
        print('Error opening the files')
        continue

    # Write the result to the output file
    if exists(f'{folderPath}/Solution.py'):
        sys.stdin = inputFile
        sys.stdout = outputFile
        spec = spec_from_file_location('Solution', f'{folderPath}/Solution.py')
        solutionModule = module_from_spec(spec)
        spec.loader.exec_module(solutionModule)
    
    # Close the files
    inputFile.close()
    outputFile.close()