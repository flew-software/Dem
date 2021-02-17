from setuptools import setup, find_packages

setup(name='Dem',
      version='1.2',
      url='https://github.com/flew-software/D',
      license='MIT',
      author='Tarith Jayasooriya',
      author_email='tarithj@gmail.com',
      description='A python library to make using lists more easy',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',  # This is important!
      zip_safe=False)
