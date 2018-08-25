import textwrap

from setuptools import setup, Extension


setup(
  name='p537',
  version='1.0.1',
  description=textwrap.dedent("""
  A tiny platform-specific distribution with a console script.

  This distribution serves as a test-case for https://github.com/pantsbuild/pex/issues/537.
  """),
  url = 'https://github.com/jsirois/p537',
  license = 'Apache License, Version 2.0',
  classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python :: 3.6',
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
