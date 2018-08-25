#include "Python.h"

static PyObject *
p537_greet(PyObject *self)
{
  PySys_WriteStdout("Hello World!");
  return Py_BuildValue(""); // None
}

static PyMethodDef p537methods[] = {
  {
    .ml_name = "greet",
    .ml_meth = (PyCFunction) p537_greet,
    .ml_flags = METH_NOARGS,
    .ml_doc = "Return a greeting string."
  },
  {NULL, NULL, 0, NULL} // Sentinel.
};

static struct PyModuleDef p537module = {
  .m_base = PyModuleDef_HEAD_INIT,
  .m_name = "p537",
  .m_doc = NULL,
  .m_size = -1,
  .m_methods = p537methods,
  .m_slots = NULL,
  .m_traverse = NULL,
  .m_clear = NULL,
  .m_free = NULL
};

PyMODINIT_FUNC
PyInit_p537(void)
{
  return PyModule_Create(&p537module);
}

