
import unittest

class TestDec2Bin(unittest.TestCase):

    def setUp(self):
        pass

    def test_0(self):
        self.assertEqual(dec2bin(0),'0')

    def test_1(self):
        self.assertEqual(dec2bin(1),'1')

    def test_2(self):
        self.assertEqual(dec2bin(2),'10')
        
def dec2bin(num):
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result
        num=num/2
    return result

if __name__ == '__main__':
    unittest.main()
    
