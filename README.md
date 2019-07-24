Python folder structure example
===============================

This sample demonstrates possible somewhat convenient way to organize
python source **code + unittest + bazel** build.

### Advantages:
* Source code is separated from tests
* Folder is "clean" from *.pyc files (when using Bazel)
* Can run both Bazel test and Python unittest

Files:
------
* sample.py - Sample python module
* BUILD - Bazel build file
* test/ - Folder with unit tests
* test/run.py - Test launcher
* test/test_*.py - Unit tests

How to build?
-------------
Build all using Bazel

    bazel build :*


How to run?
-----------
Run sample module using Bazel:

    bazel run :sample


How to test?
------------
Run all Bazel tests:

    bazel test :*

or run Bazel test suite:

    bazel test :all_tests


How to debugging tests?
-----------------------
You can also run all or particular tests using run_tests (test/run.py) launcher:

    bazel run :run_tests

See options:

    bazel run :run_tests -- -h

Increase verbosity:

    bazel run :run_tests -- -vv

Run particular test case:

    bazel run :run_tests -- test_one.TestOne

or particular test function:

    bazel run :run_tests -- test_one.TestOne.test_one

Run test function with debug logs:

    bazel run :run_tests -- test_one.TestOne.test_one -vvv


You can also run unit tests directly without Bazel with the same options:

    python test/run.py
