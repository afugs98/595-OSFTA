# File was generated with boilerplate code from ChatGPT 4

import os

class FileTreeWalker:
    def __init__(self, baseDirectory, targetDirectory):
        self.baseDirectory = baseDirectory
        self.targetDirectory = os.path.join(self.baseDirectory, targetDirectory)

    def readFile(self, filePath):
        with open(filePath, 'r') as file:
            return file.read()  # Or perform any file-specific reading logic

    def processFileData(self, fileData):
        # Process the file data as needed

        # This is where we would parse the data and construct an object for this file


        pass

    def walkDirectoryTree(self):
        for root, dirs, files in os.walk(self.targetDirectory):
            for file in files:
                if file.endswith('.cpp'):
                    filePath = os.path.join(root, file)
                    print(filePath)
                    fileData = self.readFile(filePath)
                    self.processFileData(fileData)

# Usage
if __name__ == "__main__":
    currentDirectory = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of the current file
    inputsRelativePath = os.path.join('..', 'Inputs')  # Path to 'Inputs' from 'Source'
    
    TreeWalker = FileTreeWalker(currentDirectory, inputsRelativePath)
    TreeWalker.walkDirectoryTree()
