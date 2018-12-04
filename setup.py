from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('src/be/svlandeg/compile_test_pyx_pyd/*.pyx'))