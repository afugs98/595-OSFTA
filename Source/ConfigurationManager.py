class ConfigurationManager:
    def __init__(self, config_data):
        self.root_source_directory = config_data['root_source_directory']
        self.file_extensions = config_data['file_extensions'].split(',')

def read_config_file(config_path):
    config_data = {}
    with open(config_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config_data[key] = value
    return config_data
