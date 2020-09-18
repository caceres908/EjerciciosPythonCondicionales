import unittest
import palabraCiclos

class TestpalabraCiclos(unittest.TestCase):
    def test_palindroma(self):
        palabraCiclos.palindroma("perro")
if __name__ == "__main__":
    unittest.main()


