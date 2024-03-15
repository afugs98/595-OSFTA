# This is the file that users will eventually run. 
# This serves as the main entry point into the OSFTA program

# Loosely speaking, this will examine the config file
# Then walk the file tree
# Then build the graph for compute
# Then compute
# Then show the results

import sys
import os
from Source.FileTreeWalker import *
from Source.ConfigurationManager import *




class OSFTAManager:

    def __init__(self, inputAnalysisFilepath):
        
        # Set up empty class variables to be used later
        self.configManager = None
        self.fileTreeWalker = None

        # Construct filepaths for analysis based on this directory as the root
        self.analysisFilepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), inputAnalysisFilepath)
        print(self.analysisFilepath)

    def buildConfiguration(self, configFilename):

        print('Building Configuration...')

        configFilepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), configFilename)

        # Construct ConfigurationManager as OSFTA member variable
        self.configManager = ConfigurationManager(configFilepath)


    def walkTree(self):
        print('Walking Tree...')

        # Construct the FileTreeWalker
        self.fileTreeWalker = FileTreeWalker(self.analysisFilepath)

        # Run the tree walker
        self.fileTreeWalker.walkDirectoryTree()

        pass

    def buildUnprocessedTree(self):
        # Sean, depending on how we want to do this
        # you can put your code to build the tree here.
        #
        # This may require reworking the FileTreeWalker to be 
        # "object-friendly" which I am available to do

        pass


    def processTree(self):
        # Sean, Arnab, this is where we will invoke the processing
        # to take the unprocessed tree and run FTA on it
        
        pass


    def printOutput(self):
        # Arnab, this is where you'd integrate the code to
        # print the tree that Sean has made

        pass




# Run the entire OSFTA program
if __name__ == '__main__':
    
    print('Running OSFTA...')

    analysisPath = sys.argv[1]
    configFilename = sys.argv[2]

    # Construct empty OSFTAManager
    manager = OSFTAManager(analysisPath)

    # Run config reading and steps with passed input filename
    manager.buildConfiguration(configFilename)
    
    # Walk the tree
    manager.walkTree()

    # Build the unprocessed tree
    manager.buildUnprocessedTree()

    # Process the tree
    manager.processTree()

    # Print the output
    manager.printOutput()
