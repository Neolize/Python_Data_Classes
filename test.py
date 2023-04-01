"""Tests for explore_common_mistakes.py, first_example.py and vector.py files"""

import unittest

import explore_common_mistakes
import first_examples
import vector


class TestArray(unittest.TestCase):
    def test_add_number_to_array(self):
        self.assertEqual(explore_common_mistakes.add_number_to_array(37), [37])
        self.assertEqual(explore_common_mistakes.add_number_to_array(109), [109])
        self.assertEqual(explore_common_mistakes.add_number_to_array(14, [43, 91]), [43, 91, 14])
        self.assertEqual(explore_common_mistakes.add_number_to_array(2, [6]), [6, 2])
        self.assertEqual(explore_common_mistakes.add_number_to_array(3, []), [3])


class TestToy(unittest.TestCase):

    def test_toy_instance_returned_information(self):
        toy_instance = first_examples.Toy("Clown", 1.5, 1100.0)

        self.assertEqual(toy_instance.name, "Clown")
        self.assertEqual(toy_instance.weight, 1.5)
        self.assertEqual(toy_instance.price, 1100.0)

    def test_toy_instance_returned_types(self):
        first_toy_instance = first_examples.Toy("Ball", 3, 782.5)
        second_toy_instance = first_examples.Toy("Knight", 0.3, 350)

        for item in (first_toy_instance, second_toy_instance):
            self.assertIsInstance(item.name, str)
            self.assertIsInstance(item.weight, (int, float))
            self.assertIsInstance(item.price, (int, float))


class TestToyData(unittest.TestCase):

    def test_toy_data_instance_returned_information(self):
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

    def test_toy_data_instance_returned_types(self):
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


class TestVector3D(unittest.TestCase):

    def test_vector3D_instance_returned_information(self):
        first_vector_instance = vector.Vector3D(2, 3, 4, calc_length=False)
        second_vector_instance = vector.Vector3D(3, 6, 2)
        self.assertEqual(first_vector_instance.x, 2)
        self.assertEqual(first_vector_instance.y, 3)
        self.assertEqual(first_vector_instance.z, 4)
        self.assertEqual(first_vector_instance.length, 0)

        self.assertEqual(second_vector_instance.x, 3)
        self.assertEqual(second_vector_instance.y, 6)
        self.assertEqual(second_vector_instance.z, 2)
        self.assertEqual(second_vector_instance.length, 7.0)

    def test_vector3D_instance_returned_types(self):
        first_vector_instance = vector.Vector3D(3, 2, 4, calc_length=False)
        second_vector_instance = vector.Vector3D(1, 6, 2)

        self.assertIsInstance(first_vector_instance.x, int)
        self.assertIsInstance(first_vector_instance.y, int)
        self.assertIsInstance(first_vector_instance.z, int)
        self.assertIsInstance(first_vector_instance.length, (int, float))

        self.assertIsInstance(second_vector_instance.x, int)
        self.assertIsInstance(second_vector_instance.y, int)
        self.assertIsInstance(second_vector_instance.z, int)
        self.assertIsInstance(second_vector_instance.length, (int, float))

    def test_vector3D_comparing_instances(self):
        first_vector_instance = vector.Vector3D(7, 8, 4)
        second_vector_instance = vector.Vector3D(4, 5, 1, calc_length=False)
        self.assertGreater(first_vector_instance, second_vector_instance)

        second_vector_instance.x = 10
        self.assertLess(first_vector_instance, second_vector_instance)

        first_vector_instance.x = 10
        self.assertGreater(first_vector_instance, second_vector_instance)

    def test_vector3D_recalculate_length_method(self):
        first_vector_instance = vector.Vector3D(3, 6, 2)
        self.assertEqual(first_vector_instance.length, 7)

        first_vector_instance.x, first_vector_instance.y, first_vector_instance.z = 4, 6, 12
        first_vector_instance.recalculate_length()
        self.assertEqual(first_vector_instance.length, 14)

    def test_vector3D_compare_lengths_method(self):
        first_vector_instance = vector.Vector3D(3, 2, 7)
        second_vector_instance = vector.Vector3D(4, 9, 7)
        self.assertEqual(first_vector_instance.compare_lengths(second_vector_instance), "Lengths aren't equal")

        first_vector_instance.x, first_vector_instance.y = 4, 9
        first_vector_instance.recalculate_length()
        self.assertEqual(first_vector_instance.compare_lengths(second_vector_instance), "Lengths are equal")

    def test_vector3D_multiply_length_by_given_number_method(self):
        vector_instance = vector.Vector3D(3, 6, 2)
        self.assertEqual(vector_instance.multiply_length_by_given_number(8), 56)
        self.assertEqual(vector_instance.multiply_length_by_given_number(0), 0)
        self.assertEqual(vector_instance.multiply_length_by_given_number("number"), 0)


if __name__ == "__main__":
    unittest.main()
