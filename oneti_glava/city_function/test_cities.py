import unittest
from whike import city_full

class TestCityFull(unittest.TestCase):
    
    def test_full_city(self):
        def_city = city_full('лермонтов', 'россия')
        self.assertEqual(def_city, 'Лермонтов, Россия')
    def test_full_city_popylation(self):
        def_city_popylation = city_full('пятигорск', 'россия', '45000')
        self.assertEqual(def_city_popylation, 'Пятигорск, Россия - популяция 45000')
if __name__ == '__main__':
    unittest.main()