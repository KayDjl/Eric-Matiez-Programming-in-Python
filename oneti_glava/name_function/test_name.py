import unittest
from whil import full_name

class NameTestCase(unittest.TestCase):
    
    def test_ferst_last_name(self):
        formatted_name = full_name('сергей', 'полозков')
        self.assertEqual(formatted_name, 'Сергей Полозков')
        
if __name__ == '__main__':
    unittest.main()