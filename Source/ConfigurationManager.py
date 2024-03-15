class ConfigurationManager:
    def __init__(self, configFile):

        # First open the config file and read in data
        config_data = {}
        with open(configFile, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config_data[key] = value

        self.fileExtensions = config_data['file_extensions'].split(',')

    def getConfigFileExtensions(self):
        return self.fileExtensions



