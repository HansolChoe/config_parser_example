import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('example.ini')
    print('sections', config.sections())
    print('All values Are Strings', config['All Values Are Strings'])
