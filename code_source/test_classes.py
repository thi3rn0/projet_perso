from code_source.data.data_access import DataAccess

if __name__ == '__main__':
    data_test = DataAccess()
    result = data_test.get_classes()
    print(result)
