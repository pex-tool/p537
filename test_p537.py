import contextlib
import io
import sys

import p537


@contextlib.contextmanager
def stdout():
  orig_stdout = sys.stdout
  sys.stdout = stdout = io.StringIO()
  try:
    yield stdout
  finally:
    sys.stdout = orig_stdout


def test_greet():
  with stdout() as fp:
    p537.greet()
    fp.flush()
    fp.seek(0)

    assert 'Hello World!' == fp.read()

