import textwrap

from setuptools import setup, Extension


setup(
  name='p537',
  version='1.0',
  description=textwrap.dedent("""
  A tiny platform-specific distribution with a console script.

  This distribution serves as a test-case for https://github.com/pantsbuild/pex/issues/537.
  """),
  ext_modules=[
    Extension('p537', sources=['p537module.c'])
  ],
  entry_points={
    'console_scripts': [
      'p537 = p537:greet',
    ],
  },
)
