

import unittest

import Camel_Case

class TestCamelCase(unittest.TestCase):

    def test_capitalize(self):

        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'

        for word in input_words:
            self.assertEqual(capitalized, Camel_Case.capitalize(word))


    def test_lower(self):
        # this isn't really needed, since we can assume that Python's library functions work correctly :)
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'

        for word in input_words:
            self.assertEqual(lower, Camel_Case.lowercase(word))

    def test_filter(self):
            self.assertEqual('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|', Camel_Case.Camel_Case('!"#$%&\'()*+,-./:;<=>?@[\\]^'))



    def test_camel_case(self):

        input_and_expected_outputs = {
            '' : '' ,
            'mummy' : 'mummy',
            'Daddy' : 'daddy',
            'South west' : 'southWest',
            'SOUTH WEST' : 'southWest',
        }

        for input_val in input_and_expected_outputs.keys():


            self.assertEqual(input_and_expected_outputs[input_val], Camel_Case.camel_case(input_val))



if __name__ == '__main__':
    unittest.main()







