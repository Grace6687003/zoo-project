import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.


    def test_negative_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), "Invalid")

    def test_child1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(9), 50)

    def test_teenage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(45), 150)

    
    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()
