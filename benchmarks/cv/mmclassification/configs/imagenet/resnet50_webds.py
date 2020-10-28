"""
Config File for resnet50 EC2 runs
"""
_base_ = [
    '../_base_/models/resnet50.py', '../_base_/datasets/imagenet_webds_bs64.py',
    '../_base_/schedules/imagenet_bs2048_coslr_webds.py',
    '../_base_/default_runtime_webds.py'
]
