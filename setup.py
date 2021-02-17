from setuptools import setup, find_packages

setup(name='D',
      version='1.0',
      url='https://github.com/flew-software/D',
      license='MIT',
      author='Tarith Jayasooriya',
      author_email='tarithj@gmail.com',
      description='A python library to make using lists more easy',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
