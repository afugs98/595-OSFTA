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
        self.fileManifest = None

        # Construct filepaths for analysis based on this directory as the root
        self.analysisFilepath = os.path.join(os.getcwd(), inputAnalysisFilepath)
        print(self.analysisFilepath)

    def buildConfiguration(self, configFilename):

        configFilepath = os.path.join(os.getcwd(), configFilename)

        # Construct ConfigurationManager as OSFTA member variable
        self.configManager = ConfigurationManager(configFilepath)

        print(self.configManager.getConfigFileExtensions())

    def walkTree(self):


        pass

    # def getOSFTAAnalysisDirectory(self):
    #     return self.analysisFilepath


# Run the entire OSFTA program
if __name__ == '__main__':

    analysisPath = sys.argv[1]
    configFilename = sys.argv[2]

    print('Running OSFTA...')
    
    # Construct empty OSFTAManager
    manager = OSFTAManager(analysisPath)

    # Run config reading and steps with passed input filename
    manager.buildConfiguration(configFilename)
    
    
    # config_path = 'config.txt'
    # config_manager = create_configuration_manager(config_path)
    # print(f"Root Source Directory: {config_manager.root_source_directory}")
    # print(f"File Extensions to Examine: {config_manager.file_extensions}")