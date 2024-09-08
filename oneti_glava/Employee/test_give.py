import unittest
from class_employee import Employe

class TestGiveEmploy(unittest.TestCase):
    
    def setUp(self):
        name = 'Сергей'
        last = 'Полозков'
        okla = 50000
        self.my_empl = Employe(name, last, okla)
        
    def test_give_raise(self):
        self.my_empl.give_raise()
        self.assertEqual(self.my_empl.oklad, 55000)
        
    def test_give_raise_custom(self):
        self.my_empl.give_raise(10000)
        self.assertEqual(self.my_empl.oklad, 60000)
        
if __name__ == '__main__':
    unittest.main()