from setuptools import setup

setup(
    name='PyTorch Utils',
    version='0.0',
    author='UNC Computer Vision',
    description='A library for common PyTorch operations',
    packages=[
        'pytorch_utils',
        'pytorch_utils.io',
        'pytorch_utils.viz',
        'pytorch_utils.transform',
    ],
    package_dir={
        'pytorch_utils': 'package',
        'pytorch_utils.io': 'package/io',
        'pytorch_utils.viz': 'package/viz',
        'pytorch_utils.transform': 'package/transform'
    },
)