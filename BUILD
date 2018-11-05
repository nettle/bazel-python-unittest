py_binary(
    name = "sample",
    srcs = ["sample.py"],
)

py_test(
    name = "test_one",
    srcs = ["test/test_one.py"],
    deps = ["sample"],
)

py_test(
    name = "test_two",
    srcs = ["test/test_two.py"],
    deps = ["sample"],
)

py_test(
    name = "test_three",
    srcs = ["test/test_three.py"],
    deps = ["sample"],
)

test_suite(
    name = "all_tests",
    tests = [
        "test_one",
        "test_two",
        "test_three",
    ],
)

py_library(
    name = "test_lib",
    srcs = glob(["test/*.py"]),
    deps = [
        "sample",
    ],
)

py_binary(
    name = "run_tests",
    main = "test/run.py",
    srcs = ["test/run.py"],
    deps = ["test_lib"],
)
