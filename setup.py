from setuptools import setup

setup_args = dict(
    name='p1',
    version='0.0.1',
    description='Superfoo',
    author='Matt Gregory',
    author_email='matt.gregory@oregonstate.edu',
    url='https://github.com/grovduck/appveyor_test',
    package_dir={'': '.'},
    packages=['p1'],
    zip_safe=False
)

setup(**setup_args)
