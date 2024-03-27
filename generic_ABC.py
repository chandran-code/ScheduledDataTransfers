
def transform_data():
    print("In generic_ABC")
    config = configparser.ConfigParser()
    config.read('config.ini')
    value = config['database']['host']
    print("Value is")
    print(value)

transform_data()