"""Universal launcher for unit tests"""

import argparse
import logging
import os
import sys
import unittest


def main():
    """Parse args, collect tests and run them"""
    # Add ".." to module search path
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    top_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))
    sys.path.append(top_dir)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="count",
                        help="verbosity level, use: [-v | -vv | -vvv]")
    parser.add_argument("-s", "--start-directory", default=".",
                        help="directory to start discovery ('.' default)")
    parser.add_argument("-p", "--pattern", default="test*.py",
                        help="pattern to match test files ('test*.py' default)")
    parser.add_argument("test", nargs="*",
                        help="test specs (e.g. module.TestCase.test_func)")
    args = parser.parse_args()

    if args.verbose > 2:
        logging.basicConfig(level=logging.DEBUG, format="DEBUG: %(message)s")

    loader = unittest.TestLoader()
    if args.test:
        # Add particular tests
        for test in args.test:
            suite = unittest.TestSuite()
            suite.addTests(loader.loadTestsFromName(test))
    else:
        # Find all tests
        suite = loader.discover(args.start_directory, args.pattern)

    runner = unittest.TextTestRunner(verbosity=args.verbose)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    # NOTE: True(success) -> 0, False(fail) -> 1
    exit(not main())
