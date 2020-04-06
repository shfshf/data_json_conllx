import os

from setuptools import setup

tests_requires = [
    "pytest",
    "requests",
]

install_requires = [
    "setuptools",
    "pymongo",
    "tokenizer_tools",
]

setup(name='data_json_conllx',
      version='1.0',
      description='data_json_conllx',
      url='https://github.com/shfshf/data_json_conllx',
      author='SHF',
      author_email='1316478299@qq.com',
      packages=['data_json_conllx'],
      install_requires=install_requires,
      )
