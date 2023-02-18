
from setuptools import setup, find_packages
import os

setup(
    
    name='emmy',
    version='0.1.2',
    license='MIT',
    author="Joyoforigami",
    author_email='raise-an-issue-on-github@email-is-private.com',
    packages=find_packages('.'),
    package_dir={'':'.'},
    url='https://github.com/joyoforigami/emmy',
    keywords='esolang hash',
    install_requires=[
          'xxhash',
          'numpy'
      ]

)