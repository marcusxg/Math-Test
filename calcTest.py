import unittest
from unittest.mock import patch
from io import StringIO


def calc():
    var1 = int(input('Enter a number: '))
    op = input('Enter an operator: ')
    var2 = int(input('Enter a number: '))

    if op == '+':
        print(var1 + var2)
    elif op == '-':
        print(var1 - var2)
    elif op == '*':
        print(var1 * var2)
    elif op == '/':
        print(var1 / var2)
    elif op == '%':
        print(var1 % var2)
    else:
        print('Invalid operator or number. Please Try Again')


class TestCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=["2", "+", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_output, mock_input):
        calc()
        self.assertEqual(mock_output.getvalue().strip(), "5")

    @patch('builtins.input', side_effect=["5", "-", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_output, mock_input):
        calc()
        self.assertEqual(mock_output.getvalue().strip(), "3")

    @patch('builtins.input', side_effect=["4", "*", "6"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_output, mock_input):
        calc()
        self.assertEqual(mock_output.getvalue().strip(), "24")

    @patch('builtins.input', side_effect=["10", "/", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_output, mock_input):
        calc()
        self.assertEqual(mock_output.getvalue().strip(), "5.0")

    @patch('builtins.input', side_effect=["7", "%", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_modulus(self, mock_output, mock_input):
        calc()
        self.assertEqual(mock_output.getvalue().strip(), "1")

    @patch('builtins.input', side_effect=["5", "@", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_operator(self, mock_output, mock_input):
        calc()
        self.assertEqual(
            mock_output.getvalue().strip(),
            "Invalid operator or number. Please Try Again"
        )


if __name__ == '__main__':
    unittest.main()
