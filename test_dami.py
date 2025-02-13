import unittest


# snake_case camelCase CaseCase CASECASE

class TestDami(unittest.TestCase):
    """Class description."""
    
    def test_dami(self):
       a = 1
       b = 2 
       c = a + b
       print('The Value', c)


    def test_func(self):
    # Arrange 
        a = 20
        b = 10
    # Act
        result = a + b

    # Assert
        self.assertEqual(result,  a + b)



if __name__ == "__main__":
    unittest.main()