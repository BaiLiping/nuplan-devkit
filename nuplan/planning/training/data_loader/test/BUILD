load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "skeleton_test_dataloader",
    srcs = ["skeleton_test_dataloader.py"],
    deps = [
        "//nuplan/planning/scenario_builder:scenario_filter",
        "//nuplan/planning/scenario_builder/nuplan_db:nuplan_scenario_builder",
        "//nuplan/planning/scenario_builder/nuplan_db/test:nuplan_scenario_test_utils",
        "//nuplan/planning/training/data_augmentation:kinematic_agent_augmentation",
        "//nuplan/planning/training/data_loader:datamodule",
        "//nuplan/planning/training/data_loader:log_splitter",
        "//nuplan/planning/training/preprocessing:feature_preprocessor",
        "//nuplan/planning/training/preprocessing/feature_builders:agents_feature_builder",
        "//nuplan/planning/training/preprocessing/feature_builders:raster_feature_builder",
        "//nuplan/planning/training/preprocessing/feature_builders:vector_map_feature_builder",
        "//nuplan/planning/training/preprocessing/features:raster",
        "//nuplan/planning/training/preprocessing/features:trajectory",
        "//nuplan/planning/training/preprocessing/target_builders:ego_trajectory_target_builder",
        "//nuplan/planning/training/preprocessing/test:dummy_vectormap_builder",
        "//nuplan/planning/utils/multithreading:worker_pool",
    ],
)

py_test(
    name = "test_dataloader_ray",
    size = "small",
    srcs = ["test_dataloader_ray.py"],
    deps = [
        ":skeleton_test_dataloader",
        "//nuplan/planning/utils/multithreading:worker_ray",
    ],
)

py_test(
    name = "test_dataloader_sequential",
    size = "small",
    srcs = ["test_dataloader_sequential.py"],
    deps = [
        ":skeleton_test_dataloader",
        "//nuplan/planning/utils/multithreading:worker_sequential",
    ],
)
