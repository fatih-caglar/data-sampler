import unittest
from src import dataset 

class DatasetColumnsCheck(unittest.TestCase): 
    
    def test_empty_object(self):
        '''Column list or CSV file check'''
        self.assertRaises(dataset.EmptyColumnError, dataset.Dataset )
    

if __name__ == "__main__":
    unittest.main()
