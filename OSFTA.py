# This is the file that users will eventually run. 
# This serves as the main entry point into the OSFTA program

# Loosely speaking, this will examine the config file
# Then walk the file tree
# Then build the graph for compute
# Then compute
# Then show the results

from Source.FileTreeWalker import *
from Source.ConfigurationManager import *



class OSFTAManager:
    def __init__(self):
        self.configManager = None
        self.fileManifest = None

    def buildConfiguration(self, configFile):




        pass

    def walkTree(self):


        pass


# Run the entire OSFTA program
if __name__ == '__main__':

    print('Running OSFTA...')
    
    # Construct empty OSFTAManager
    manager = OSFTAManager()

    # Run config reading and steps
    manager.buildConfiguration('config.txt')
    
    
    # config_path = 'config.txt'
    # config_manager = create_configuration_manager(config_path)
    # print(f"Root Source Directory: {config_manager.root_source_directory}")
    # print(f"File Extensions to Examine: {config_manager.file_extensions}")