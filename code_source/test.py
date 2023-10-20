from code_source.data.data_access import DataAccess

if __name__ == '__main__':
    data = DataAccess()
    tester = DataAccess.all_modules(data)
    print(tester)