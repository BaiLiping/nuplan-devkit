load("@rules_python//python:defs.bzl", "py_test")

package(default_visibility = ["//visibility:public"])

py_test(
    name = "test_submission_container",
    size = "small",
    srcs = ["test_submission_container.py"],
    deps = [
        "//nuplan/submission:submission_container",
    ],
)

py_test(
    name = "test_challenge_servicers",
    size = "small",
    srcs = ["test_challenge_servicers.py"],
    deps = [
        "//nuplan/submission:challenge_pb2",
        "//nuplan/submission:challenge_servicers",
    ],
)

py_test(
    name = "test_submission_planner",
    size = "small",
    srcs = ["test_submission_planner.py"],
    deps = [
        "//nuplan/submission:submission_planner",
    ],
)

py_test(
    name = "test_submission_container_factory",
    size = "small",
    srcs = ["test_submission_container_factory.py"],
    deps = [
        "//nuplan/submission:submission_container_factory",
    ],
)

py_test(
    name = "test_utils",
    size = "small",
    srcs = ["test_utils.py"],
    deps = [
        "//nuplan/submission:utils",
    ],
)
