# File was generated with boilerplate code from ChatGPT 4

import os
import re
from Source.Component import UnprocessedComponent
from Source.AnalyzeEngine import AnalyzeEngine
from Source.FaultTree import FaultTree

class FileTreeWalker:
    def __init__(self, targetDirectory, fileExtensionsList):
        self.targetDirectory = targetDirectory

        self.fileExtensions = fileExtensionsList


    def readFile(self, filePath):
        with open(filePath, 'r') as file:
            return file.read()  # Or perform any file-specific reading logic


    def processFileData(self, fileData, fileExtension):
        # Process the file data as needed. This is where we would parse the data and construct an object for this file

        # Get the list of comment blocks
        parsedComments = self.parseComments(fileData, fileExtension)

        # Take just the first element, there should only be one
        # Todo, change this later to work with only one
        if parsedComments:
            parsedCommentDict = parsedComments[0]

            print("Component ID:", parsedCommentDict['id'])
            print("Failure Prob:", parsedCommentDict['failure_probability'])
            print("Dependencies:", parsedCommentDict['dependencies'])
        
            return UnprocessedComponent(id=parsedCommentDict['id'], fail_rate=parsedCommentDict['failure_probability'], unprocessed_dep=parsedCommentDict['dependencies'])
        # This is where we will create objects according to the class structure...
        return None

    def walkDirectoryTree(self):
        unprocComponents = {}
        print(self.targetDirectory)
        for root, dirs, files in os.walk(self.targetDirectory):
            print(files)
            for file in files:
                if any(file.endswith(ext) for ext in self.fileExtensions):
                    filePath = os.path.join(root, file)
                    print(filePath)

                    # Get file contents
                    fileData = self.readFile(filePath)

                    # Get the extension
                    _, fileExtension = os.path.splitext(file)

                    # Pass to processor to read filedata and parse comment blocks 
                    unprocessed = self.processFileData(fileData, fileExtension)

                    if unprocessed:
                        unprocComponents[unprocessed.id] = unprocessed
                    else:
                        print("Error with file", file)

        return unprocComponents


    ########### Lines for parsing the files found by the tree walker ###########
                    

    def parseComments(self, code, fileExtension):

        # First find every matching block, although there should only be one
        # Todo, maybe remove this and enforce there can only be one block?
        commentBlocks = self.extractCommentBlocks(code, fileExtension)

        # Parse each comment block
        # Todo, remove this if we enforce only having one block
        parsedData = [self.parseBlock(comment) for comment in commentBlocks]
        return [data for data in parsedData if data]

    def extractCommentBlocks(self, code, fileExtension):

        # Find a general "block" of potential comments with FTA data
        # This code checks for C style first, then tries to do Python if that does not resolve
        # Potentially room for improvement later

        cCommentPattern = r'/\*\*([\s\S]*?)\*/'
        firstTryCStyle = re.findall(cCommentPattern, code)

        # If the C style doesn't find anything, try Python
        if len(firstTryCStyle) == 0:
            
            pythonCommentPattern = r"'''(.*?)'''"

            secondTryPythonStyle = re.findall(pythonCommentPattern, code, re.DOTALL)

            # Returns an empty array if not found
            return secondTryPythonStyle
        
        return firstTryCStyle

    def parseBlock(self, comment):

        # Create output return dict and populate the data on each line into the dict
        data = {}
        data['id'] = self.extractParameter(comment, r'@id\s+(\S+)')
        data['failure_probability'] = self.extractParameter(comment, r'@failure-probability\s+([\d\.]+)')
        data['dependencies'] = self.extractParameter(comment, r'@dependencies\s+\[([^\]]*)\]')  

        # Handle dependencies differently since there are multiple items
        # Todo, make this also somehow parse AND and OR statements
        if all(key in data for key in ['id', 'failure_probability', 'dependencies']):
            if data['dependencies']:
                data['dependencies'] = data['dependencies'].strip()
            else:
                data['dependencies'] = None
            return data
        return None


    def extractParameter(self, comment, pattern):

        # Just looks for a certain regex string and passes the result back if it found it
        match = re.search(pattern, comment)
        return match.group(1) if match else None

# Usage if the file is the main file, not the regular intent
if __name__ == "__main__":
    
    # Gets the directory of the current file
    currentDirectory = os.path.dirname(os.path.abspath(__file__))  

    # First do the C example
    inputsRelativePath = os.path.join('..', 'Inputs', 'BuildingController')  # Path to 'Inputs' from 'Source'
    TreeWalker = FileTreeWalker(os.path.join(currentDirectory, inputsRelativePath), [".cpp"])    
    dic = TreeWalker.walkDirectoryTree()
    Analyzer = AnalyzeEngine()
    dic = Analyzer.createUnprocessedTree(dic)
    root = Analyzer.root
    tree = FaultTree(root)
    tree.print_tree()

    # Second do the Python example
    inputsRelativePath = os.path.join('..', 'Inputs', 'PythonSatelliteController')  # Path to 'Inputs' from 'Source'

    print(inputsRelativePath)
    
    TreeWalker = FileTreeWalker(os.path.join(currentDirectory, inputsRelativePath), [".py"])    
    dic = TreeWalker.walkDirectoryTree()
    
    Analyzer = AnalyzeEngine()
    dic = Analyzer.createUnprocessedTree(dic)
    
    root = Analyzer.root
    tree = FaultTree(root)
    # tree.print_tree()
