from setuptools import setup, Extension


def long_description():
  with open('README.rst') as fp:
    return fp.read()


setup(
  name='p537',
  version='1.0.5',
  author="John Sirois",
  author_email="john.sirois@gmail.com",
  description='A tiny platform-specific distribution with a console script.',
  long_description=long_description(),
  long_description_content_type="text/x-rst",
  url='https://github.com/jsirois/p537',
  license='Apache License, Version 2.0',
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  ext_modules=[
    Extension('p537', sources=['p537module.c']),
  ],
  entry_points={
    'console_scripts': [
      'p537 = p537:greet',
    ],
  },
)
