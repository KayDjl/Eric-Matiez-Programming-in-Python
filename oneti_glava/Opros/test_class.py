import unittest
from class_incript import AnonimnyOpros

class test_class_opros(unittest.TestCase):
    
    def test_class(self):
        anon = 'Какие языки вы знаете: '
        my_opros = AnonimnyOpros(anon)
        my_opros.save_with('Русский')
        self.assertIn('Русский', my_opros.listion)
    
    def test_three_class(self):
        anon = 'Какие языки вы знаете: '
        my_opros = AnonimnyOpros(anon)
        listion = ['English', 'Russion', 'Arabico']
        for lists in listion:
            my_opros.save_with(lists)
        for lists in listion:
            self.assertIn(lists, my_opros.listion)
        
if __name__ == '__main__':
    unittest.main()