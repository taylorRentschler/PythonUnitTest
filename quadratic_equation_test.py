import unittest
import quadratic_equation


class QuadraticEquationTest(unittest.TestCase):
    def test_positive(self):
        """ This tests when the discriminant has 2 real, positive values.
            (b^2 - 4 * a * c) > 0 """
        
        positive_solution, negative_solution = \
            quadratic_equation.quadratic_equation(5, 6, 1)
        self.assertEqual(positive_solution.real, -0.2)
        self.assertEqual(negative_solution.real, -1)

    #@unittest.skip("Test not developed")
    def test_zero(self):
        """ This tests when the discriminant is equal to zero.
            (b^2 - 4 * a * c) = 0 """
        
        positive_solution, negative_solution = \
            quadratic_equation.quadratic_equation(4, 4, 1)
        self.assertEqual(positive_solution.real, -.5)
        self.assertEqual(negative_solution.real, -.5)

        #Code needs a way to check if only 1 solution exists
        # and return only the != 0 solution. 


    @unittest.skip("Test not developed")
    def test_negative(self):
        """ This tests when the discriminant is negative.
            (b^2 - 4 * a * c) < 0 """
        
        positive_solution, negative_solution = \
            quadratic_equation.quadratic_equation(6, 5, 2)

    def test_divide_by_zero(self):
        """ This tests when the a divide by zero would occur.
            (a=0) """
        
        with self.assertRaises(ZeroDivisionError):
            positive_solution, negative_solution = \
                quadratic_equation.quadratic_equation(0, 6, 1)


if __name__ == '__main__':
    unittest.main()
