import unittest
import argparse
import sys
from que1 import verify_pincode


#Perform Unit Test
class TestVerifyPincodeFromFile(unittest.TestCase):    

    def load_test_cases(filename):
        test_cases = []
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                address = parts[0].strip()
                expected_result = parts[1].strip() == 'true'
                test_cases.append((address, expected_result))
        return test_cases

def create_test_method(address, expected_result):
    def test(self):
        result = verify_pincode(address)
        self.assertEqual(result, expected_result, f"Address: '{address}' is expected to be {'valid' if expected_result else 'invalid'}")
    return test

def main():
    
    # Get inputs from command line
    parser = argparse.ArgumentParser(description='Run pincode verification tests from a file')
    parser.add_argument('testfile', help='Path to the test file containing test cases')
    parser.add_argument('outputfile', help='Path to the output file')

    args = parser.parse_args()

    test_loader = unittest.TestLoader()

    # Create a test suite with dynamically generated test methods
    test_suite = unittest.TestSuite()
    counter = 0
    for address, expected_result in TestVerifyPincodeFromFile.load_test_cases(args.testfile):
        test_method = create_test_method(address, expected_result)
        test_name = f"test_case_{counter}"
        dynamic_test_case = type('DynamicTestCase', (TestVerifyPincodeFromFile,), {test_name: test_method})
        test_suite.addTest(test_loader.loadTestsFromTestCase(dynamic_test_case))
        counter += 1


    # Redirect the standard output to both the console and write it in test report
    original_stdout = sys.stdout

    with open(args.outputfile, 'w') as output_file:
        sys.stdout = sys.__stdout__ = output_file
        test_runner = unittest.TextTestRunner(verbosity=2, stream=output_file)
        result = test_runner.run(test_suite)

    # Restore the original standard output
    sys.stdout = sys.__stdout__ = original_stdout

    # Display the captured output in the console
    print()
    with open(args.outputfile, 'r') as output_file:
        print(output_file.read(), end='')
        
    # Exit with an appropriate status code (0 for success, 1 for failure)
    if not result.wasSuccessful():
        exit(1)
        
    exit(0)


if __name__ == '__main__':
    main()