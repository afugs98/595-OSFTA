# File was generated with boilerplate code from ChatGPT 4

import os
import re

class FileTreeWalker:
    def __init__(self, baseDirectory, targetDirectory):
        self.baseDirectory = baseDirectory
        self.targetDirectory = os.path.join(self.baseDirectory, targetDirectory)

    def readFile(self, filePath):
        with open(filePath, 'r') as file:
            return file.read()  # Or perform any file-specific reading logic

    def processFileData(self, fileData):
        # Process the file data as needed. This is where we would parse the data and construct an object for this file

        # Get the list of comment blocks
        parsedComments = self.parseComments(fileData)

        # Take just the first element, there should only be one
        # Todo, change this later to work with only one
        if parsedComments:
            parsedCommentDict = parsedComments[0]

            print("Component ID:", parsedCommentDict['id'])
            print("Failure Prob:", parsedCommentDict['failure_probability'])
            print("Dependencies:", parsedCommentDict['dependencies'])
        

        # This is where we will create objects according to the class structure...



    def walkDirectoryTree(self):
        for root, dirs, files in os.walk(self.targetDirectory):
            for file in files:
                if file.endswith('.cpp'):
                    filePath = os.path.join(root, file)
                    print(filePath)

                    # Get file contents
                    fileData = self.readFile(filePath)

                    # Pass to processor to read filedata and parse comment blocks 
                    self.processFileData(fileData)


    ########### Lines for parsing the files found by the tree walker ###########
                    

    def parseComments(self, code):

        # First find every matching block, although there should only be one
        # Todo, maybe remove this and enforce there can only be one block?
        commentBlocks = self.extractCommentBlocks(code)

        # Parse each comment block
        # Todo, remove this if we enforce only having one block
        parsedData = [self.parseBlock(comment) for comment in commentBlocks]
        return [data for data in parsedData if data]

    def extractCommentBlocks(self, code):

        # Find a general "block" of potential comments with FTA data
        blockCommentPattern = r'/\*\*([\s\S]*?)\*/'
        return re.findall(blockCommentPattern, code)

    def parseBlock(self, comment):

        # Create output return dict and populate the data on each line into the dict
        data = {}
        data['id'] = self.extractParameter(comment, r'@id\s+(\S+)')
        data['failure_probability'] = self.extractParameter(comment, r'@failure-probability\s+([\d\.]+)')
        data['dependencies'] = self.extractParameter(comment, r'@dependencies\s+\[([^\]]*)\]')  

        # Handle dependencies differently since there are multiple items
        # Todo, make this also somehow parse AND and OR statements
        if all(key in data for key in ['id', 'failure_probability', 'dependencies']):
            data['dependencies'] = [dep.strip() for dep in data['dependencies'].split(',')] if data['dependencies'] else []
            return data
        return None


    def extractParameter(self, comment, pattern):

        # Just looks for a certain regex string and passes the result back if it found it
        match = re.search(pattern, comment)
        return match.group(1) if match else None

# Usage if the file is the main file, not the regular intent
if __name__ == "__main__":
    currentDirectory = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of the current file
    inputsRelativePath = os.path.join('..', 'Inputs')  # Path to 'Inputs' from 'Source'
    
    TreeWalker = FileTreeWalker(currentDirectory, inputsRelativePath)
    TreeWalker.walkDirectoryTree()
