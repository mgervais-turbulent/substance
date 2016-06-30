from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

execfile('substance/_version.py')

install_requires = ['setuptools>=1.1.3', 'PyYAML', 'tabulate', 'paramiko', 'netaddr', 'requests', 'tinydb', 'python_hosts', 'jinja2']

setup(name='substance',
      version=__version__,
      author='turbulent/bbeausej',
      author_email='b@turbulent.ca',
      license='MIT',
      long_description=readme,
      description='substance - local dockerized development environment',
      install_requires=install_requires,
      packages=find_packages(),
      package_data={ 'substance': ['support/*'] },
      test_suite='tests',
      zip_safe=False,
      entry_points={
        'console_scripts': [
          'substance = substance.cli:cli',
          'subenv = substance.subenv.cli:cli'
        ],
      })
