import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

minCost = Solution.minCost

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(minCost(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        print('Test Case 1:')
        self.run_test([[[17,2,17],[16,16,5],[14,3,19]]], 10)
    
    @timeout(2)
    def test_case_2(self):
        print('Test Case 2:')
        self.run_test([[[7,6,2]]], 2)

    @timeout(2)
    def test_case_3(self):
        print('Test Case 3:')
        self.run_test([[[14, 5, 19], [2, 16, 11], [7, 8, 13], [10, 12, 6], [15, 4, 9], [18, 3, 20], [1, 17, 14], [6, 11, 5], [12, 19, 2], [8, 7, 16], [3, 14, 10], [13, 1, 15], [11, 20, 4], [9, 18, 7], [5, 2, 12], [17, 6, 8], [20, 9, 3], [4, 13, 1], [16, 10, 17], [19, 15, 18]]], 123)
    

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()