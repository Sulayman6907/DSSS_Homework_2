import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        min_val, max_val = 1, 10
        random_int = generate_random_integer(min_val, max_val)
        self.assertTrue(min_val <= random_int <= max_val)

    def test_generate_random_operator(self):
        operators = ['+', '-', '*']
        random_op = generate_random_operator()
        self.assertIn(random_op, operators)

    def test_calculate_result(self):
        n1, n2, operator = 5, 3, '+'
        result = calculate_result(n1, n2, operator)
        self.assertEqual(result, n1 + n2)

        n1, n2, operator = 7, 2, '-'
        result = calculate_result(n1, n2, operator)
        self.assertEqual(result, n1 - n2)

        n1, n2, operator = 4, 6, '*'
        result = calculate_result(n1, n2, operator)
        self.assertEqual(result, n1 * n2)

if __name__ == '__main__':
    unittest.main()
