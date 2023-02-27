import unittest
from Die import Die

class TestDieFunctions(unittest.TestCase):
    def Setup(self):
        self.die1 = Die()
        self.die2 = Die(8)
        
        
    def test_init(self):
        self.assertEqual(self.die, 6)
        self.assertEqual(self.die2, 8)
        
if __name__ == '__main__':
    unittest.main()

