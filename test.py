import unittest

import explore_common_mistakes


class TestArray(unittest.TestCase):
    def test_add_number_to_array(self):
        self.assertEqual(explore_common_mistakes.add_number_to_array(37), [37])
        self.assertEqual(explore_common_mistakes.add_number_to_array(109), [109])
        self.assertEqual(explore_common_mistakes.add_number_to_array(14, [43, 91]), [43, 91, 14])
        self.assertEqual(explore_common_mistakes.add_number_to_array(2, [6]), [6, 2])
        self.assertEqual(explore_common_mistakes.add_number_to_array(3, []), [3])


if __name__ == "__main__":
    unittest.main()
