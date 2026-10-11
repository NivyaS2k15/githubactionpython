import unittest
from parking import should_open_barrier


class TestParking(unittest.TestCase):

    def test_near_object(self):
        self.assertTrue(should_open_barrier(5))

    def test_far_object(self):
        self.assertFalse(should_open_barrier(15))

    def test_boundary(self):
        self.assertFalse(should_open_barrier(10))

    def test_invalid_reading(self):
        self.assertFalse(should_open_barrier(None))
        self.assertFalse(should_open_barrier(-1))


if __name__ == "__main__":
    unittest.main()