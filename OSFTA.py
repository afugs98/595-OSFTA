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
