class ConfigurationManager:
    def __init__(self, configFile):

        # First open the config file and read in data
        config_data = {}
        with open(configFile, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config_data[key] = value

        # Return the list of file extensions
        # Unless the string showing the file extensions is empty, then return an empty array
        self.fileExtensions = [] if config_data['file_extensions'] == '' else config_data['file_extensions'].split(',')


    def getConfigFileExtensions(self):
        return self.fileExtensions





