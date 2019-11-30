import unittest
from flight_functions import is_valid_flight_sequence

# You can use this data in your tests if you want to
SMALL_ROUTES_DICT = {'AA1': {'AA2', 'AA3'}}
# You can (and should) also create and use other RouteDicts for your tests
TEST_ROUTES_DICT_FOUR_CITIES = {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1', 'AA5'}, 'AA5': {'AA4', 'AA2', 'AA6'}, 
    'AA6': {'AA1', 'AA3', 'AA5', 'AA7'}, 
    'AA7': {'AA8', 'AA9'}, 'AA8': {'AA9'}, 'AA9': {}}

class TestIsValidFlightSequence(unittest.TestCase):

    def test_valid_direct_flight(self):
        expected = True
        sequence = ['AA1', 'AA2']
        actual = is_valid_flight_sequence(sequence, SMALL_ROUTES_DICT)
        self.assertEqual(actual, expected)
        
    # Add tests below to create a complete set of tests without redundant tests
    # Redundant tests are tests that would only catch bugs that another test
    # would also catch.
    def test_is_valid_flight_sequence_empty_str(self):
        """Test is_valid_flight_sequence with a sequence containing only one
        string.
        """
        expected = False
        sequence = []
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)    
    
    def test_is_valid_flight_sequence_one_str(self):
        """Test is_valid_flight_sequence with a sequence containing only one
        string.
        """
        expected = False
        sequence = ['AA3']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
    
    def test_is_valid_flight_sequence_less_str(self):
        """Test is_valid_flight_sequence with a sequence containing small amount
        of strings
        """
        expected = True
        sequence = ['AA1', 'AA2', 'AA3', 'AA4']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
        
    def test_is_valid_flight_sequence_more_str(self):
        """Test is_valid_flight_sequence with a sequence containing large amount
        of strings
        """
        expected = True
        sequence = ['AA1', 'AA2', 'AA3', 'AA4', 'AA5', 'AA6', 'AA7', 'AA8', \
                    'AA9']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected) 
        
    def test_is_valid_flight_sequence_one_wrong_str(self):
        """Test is_valid_flight_sequence with a sequence containing many strings
        that one string are not a destination of the previous one.
        """
        expected = False
        sequence = ['AA1', 'AA2', 'AA4', 'AA3']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
    
    def test_is_valid_flight_sequence_more_wrong_str(self):
        """Test is_valid_flight_sequence with a sequence containing many strings
        that one string are not a destination of the previous one.
        """
        expected = False
        sequence = ['AA1', 'AA7', 'AA4', 'AA3']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
        
    def test_is_valid_flight_sequence_last_wrong_str(self):
        """Test is_valid_flight_sequence with a sequence with the last pair of 
        IATA codes that does not have flights from the previous one to the last
        one.
        """
        expected = False
        sequence = ['AA1', 'AA2', 'AA3', 'AA4', 'AA5', 'AA6', 'AA8', 'AA1']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)    
        
    def test_is_valid_flight_sequence_first_wrong_str(self):
        """Test is_valid_flight_sequence with a sequence with the first str
        is not a source in route information.
        """
        expected = False
        sequence = ['BB1', 'AA7', 'AA4', 'AA3']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)        
        
    def test_is_valid_flight_sequence_middle_wrong(self):
        """Test is_valid_flight_sequence with strings in the middle not in routes.
        """
        expected = False
        sequence = ['AA1', 'BB2', 'CC5', 'AA5']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
        
    def test_is_valid_flight_sequence_last_not_exist(self):
        """Test is_valid_flight_sequence with strings in the middle not in routes.
        """
        expected = False
        sequence = ['AA1', 'AA2', 'AA3', 'BB5']
        actual = is_valid_flight_sequence(sequence, \
                                          TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)    

if __name__ == '__main__':
    unittest.main(exit=False)
