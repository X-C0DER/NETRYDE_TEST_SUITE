from pages.TestDataMgr import TestDataManager

def load_test_data2():
    TestDataMGR=TestDataManager()        
    test_data=TestDataMGR.prepare_all_test_data()
    return test_data