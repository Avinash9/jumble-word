import unittest
from Solver import *

class TestSolver(unittest.TestCase):
    
    
    def testListOfWords(self):
        test_list=['apple','joy','toy','hello','temple']
        get_dict=get_words_dict(3, test_list)
        self.assertEquals(2, len(get_dict))
        get_dict=get_words_dict(6, test_list)
        self.assertEquals(1, len(get_dict))
        
    def testPossibleOutput(self):
        test_list=['ant','apple','tan','kite','kitetan','hello','nat']
        get_possible_outcome=find_possible_words('ant', test_list)
        self.assertEquals(3, len(get_possible_outcome))