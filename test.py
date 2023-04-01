import unittest

import explore_common_mistakes
import first_examples


class TestArray(unittest.TestCase):
    def test_add_number_to_array(self):
        self.assertEqual(explore_common_mistakes.add_number_to_array(37), [37])
        self.assertEqual(explore_common_mistakes.add_number_to_array(109), [109])
        self.assertEqual(explore_common_mistakes.add_number_to_array(14, [43, 91]), [43, 91, 14])
        self.assertEqual(explore_common_mistakes.add_number_to_array(2, [6]), [6, 2])
        self.assertEqual(explore_common_mistakes.add_number_to_array(3, []), [3])


class TestToy(unittest.TestCase):

    def test_toy_instance_return_information(self):
        toy_instance = first_examples.Toy("Clown", 1.5, 1100.0)

        self.assertEqual(toy_instance.name, "Clown")
        self.assertEqual(toy_instance.weight, 1.5)
        self.assertEqual(toy_instance.price, 1100.0)

    def test_toy_return_types(self):
        first_toy_instance = first_examples.Toy("Ball", 3, 782.5)
        second_toy_instance = first_examples.Toy("Knight", 0.3, 350)

        for item in (first_toy_instance, second_toy_instance):
            self.assertIsInstance(item.name, str)
            self.assertIsInstance(item.weight, (int, float))
            self.assertIsInstance(item.price, (int, float))


class TestToyData(unittest.TestCase):

    def test_toy_data_instance_return_information(self):
        first_toy_data_instance = first_examples.ToyData("Dinosaur", 0.3, 293, ["plastic"])
        second_toy_data_instance = first_examples.ToyData()

        self.assertEqual(first_toy_data_instance.name, "Dinosaur")
        self.assertEqual(first_toy_data_instance.weight, 0.3)
        self.assertEqual(first_toy_data_instance.price, 293)
        self.assertEqual(first_toy_data_instance.materials, ["plastic"])

        self.assertEqual(second_toy_data_instance.name, "Nameless")
        self.assertEqual(second_toy_data_instance.weight, 0)
        self.assertEqual(second_toy_data_instance.price, 0)
        self.assertEqual(second_toy_data_instance.materials, [])

    def test_toy_data_return_types(self):
        first_toy_data_instance = first_examples.ToyData("Car", 1.1, 461.7, ["iron", "glass"])
        second_toy_data_instance = first_examples.ToyData()

        self.assertIsInstance(first_toy_data_instance.name, str)
        self.assertIsInstance(first_toy_data_instance.weight, (int, float))
        self.assertIsInstance(first_toy_data_instance.price, (int, float))
        self.assertIsInstance(first_toy_data_instance.materials, list)

        self.assertIsInstance(second_toy_data_instance.name, str)
        self.assertIsInstance(second_toy_data_instance.weight, (int, float))
        self.assertIsInstance(second_toy_data_instance.price, (int, float))
        self.assertIsInstance(second_toy_data_instance.materials, list)

    def test_toy_data_comparing_instances(self):
        first_toy_data_instance = first_examples.ToyData("Ship", 2, 2800, ["plastic", "iron"])
        second_toy_data_instance = first_examples.ToyData()

        self.assertGreater(first_toy_data_instance, second_toy_data_instance)

        second_toy_data_instance.price = 3500
        self.assertLess(first_toy_data_instance, second_toy_data_instance)

        first_toy_data_instance.price = 3500
        self.assertEqual(first_toy_data_instance, second_toy_data_instance)


if __name__ == "__main__":
    unittest.main()
