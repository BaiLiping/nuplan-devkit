load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "challenge_pb2",
    srcs = ["challenge_pb2.py"],
)

py_library(
    name = "challenge_pb2_grpc",
    srcs = ["challenge_pb2_grpc.py"],
    deps = [
        ":challenge_pb2",
    ],
)

py_library(
    name = "proto_converters",
    srcs = ["proto_converters.py"],
    deps = [
        ":challenge_pb2",
        "//nuplan/common/actor_state:ego_state",
        "//nuplan/common/actor_state:state_representation",
        "//nuplan/common/actor_state:vehicle_parameters",
        "//nuplan/common/maps/nuplan_map:map_factory",
        "//nuplan/planning/simulation/trajectory:abstract_trajectory",
        "//nuplan/planning/simulation/trajectory:interpolated_trajectory",
    ],
)

py_library(
    name = "challenge_servicers",
    srcs = ["challenge_servicers.py"],
    deps = [
        ":challenge_pb2",
        ":challenge_pb2_grpc",
        ":proto_converters",
        "//nuplan/common/actor_state:state_representation",
        "//nuplan/common/maps:map_manager",
        "//nuplan/planning/simulation/planner:abstract_planner",
    ],
)

py_library(
    name = "submission_container",
    srcs = ["submission_container.py"],
    deps = [
        "//nuplan/common/utils:helpers",
    ],
)

py_library(
    name = "submission_container_factory",
    srcs = ["submission_container_factory.py"],
    deps = [
        ":submission_container",
    ],
)

py_library(
    name = "submission_container_manager",
    srcs = ["submission_container_manager.py"],
    deps = [
        ":submission_container",
        ":submission_container_factory",
    ],
)

py_library(
    name = "submission_planner",
    srcs = ["submission_planner.py"],
    deps = [
        ":challenge_pb2_grpc",
        ":challenge_servicers",
        "//nuplan/common/maps:map_manager",
        "//nuplan/common/maps/nuplan_map:map_factory",
        "//nuplan/database/maps_db:gpkg_mapsdb",
        "//nuplan/planning/simulation/planner:abstract_planner",
        "//nuplan/planning/simulation/planner:simple_planner",
    ],
)

py_library(
    name = "utils",
    srcs = ["utils.py"],
    deps = [],
)
