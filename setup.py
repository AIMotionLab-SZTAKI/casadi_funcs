from setuptools import setup, find_packages

setup(name="casadi_funcs",
      packages=find_packages(),
      version='1.0.0',
      install_requires=[
        "numpy>=1.20.0",
        "casadi~=3.6.0",
        "scipy>=1.7.0"
        ]
      )